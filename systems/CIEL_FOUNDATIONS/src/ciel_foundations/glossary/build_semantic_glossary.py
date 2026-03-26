from __future__ import annotations

import csv
import json
import sqlite3
import textwrap
from collections import Counter
from pathlib import Path

import yaml


def slug(s: str) -> str:
    import re
    s = s.lower().replace('^', '').replace('/', '-').replace(' ', '-')
    s = re.sub(r'[^a-z0-9._-]+', '-', s)
    s = re.sub(r'-+', '-', s).strip('-')
    return s


def build(repo: Path) -> dict:
    found = repo / 'systems/CIEL_FOUNDATIONS'
    omega = repo / 'systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega'
    axioms_registry_path = found / 'axioms/registry.yaml'
    constants_registry_path = found / 'constants/registry.yaml'
    vocab_path = omega / 'vocabulary.yaml'
    b1b2_path = repo / 'research/holonomy_closure_b1_b2/results.json'
    orbital_geom_path = repo / 'reports/global_orbital_coherence_pass/real_geometry.json'

    cards_dir = found / 'definitions/cards'
    generated_dir = omega / 'vocabulary/generated'
    reports_dir = repo / 'reports/glossary'
    for d in [cards_dir, generated_dir, reports_dir, found / 'definitions/tables']:
        d.mkdir(parents=True, exist_ok=True)

    axioms_reg = yaml.safe_load(axioms_registry_path.read_text())
    constants_reg = yaml.safe_load(constants_registry_path.read_text())
    vocab = yaml.safe_load(vocab_path.read_text())
    json.loads(b1b2_path.read_text())
    json.loads(orbital_geom_path.read_text())

    tag_taxonomy = {
        'prefixes': {
            'type': 'high-level glossary card type',
            'domain': 'project sector or scientific scope',
            'status': 'epistemic status inside the repo',
            'role': 'primary formal role',
            'layer': 'where the object lives in the stack',
            'bind': 'runtime or registry availability',
            'math': 'mathematical structure involved',
            'sector': 'physics/runtime sector',
        },
        'allowed_examples': [
            'type:axiom', 'type:constant', 'type:operator', 'type:constraint', 'type:coupling',
            'type:effect', 'type:space', 'type:formalism', 'type:observable', 'type:topology',
            'domain:foundations', 'domain:omega', 'domain:metatime', 'domain:runtime', 'domain:semantics',
            'status:axiom', 'status:operational', 'status:working_definition', 'status:measured', 'status:research_note', 'status:hypothesis',
            'role:closure', 'role:holonomy', 'role:phase', 'role:identity', 'role:transport', 'role:cp', 'role:memory', 'role:seed',
            'bind:runtime', 'bind:registry', 'bind:derived', 'bind:none',
            'math:hilbert', 'math:projective', 'math:connection', 'math:curvature', 'math:spectrum', 'math:lagrangian', 'math:topology',
            'sector:neutrino', 'sector:memory', 'sector:cosmology', 'sector:omega'
        ]
    }
    (found / 'definitions/tags.yaml').write_text(yaml.safe_dump(tag_taxonomy, sort_keys=False, allow_unicode=True))

    cards = []

    axiom_formals = {
        'AX-001': '[psi] in CP^n ; physical state = phase-equivalence class',
        'AX-002': 'Only closure-admissible phase configurations are dynamically stable',
        'AX-003': 'spec(T) defines identity; labels alone do not',
        'AX-004': 'Arithmetic seeds define admissible initial spectral structure',
        'AX-005': 'Constants emerge as closure invariants, not external inserts',
    }
    axiom_tags = {
        'AX-001': ['type:axiom','domain:foundations','status:axiom','role:state','layer:foundations','bind:registry','math:projective'],
        'AX-002': ['type:axiom','domain:foundations','status:axiom','role:closure','layer:foundations','bind:registry','math:topology'],
        'AX-003': ['type:axiom','domain:foundations','status:axiom','role:spectrum','layer:foundations','bind:registry','math:spectrum'],
        'AX-004': ['type:axiom','domain:foundations','status:axiom','role:seed','layer:foundations','bind:registry','math:topology'],
        'AX-005': ['type:axiom','domain:foundations','status:axiom','role:constant','layer:foundations','bind:registry','math:topology'],
    }
    for ax in axioms_reg['axioms']:
        aid = ax['id']
        cards.append({
            'stable_id': f'GLOSS-{aid}',
            'canonical_id': f'axiom.{aid.lower()}',
            'symbol': aid,
            'name': ax['name'],
            'card_type': 'axiom',
            'class': 'axiom',
            'subclass': None,
            'status': 'axiom',
            'certainty_scope': 'internal_frozen_axiom',
            'formula': axiom_formals[aid],
            'units': 'n/a',
            'value': None,
            'numeric_value': None,
            'description': ax['summary'],
            'tags': axiom_tags[aid],
            'relational_couplings': [],
            'cross_refs': [],
            'source_paths': ['systems/CIEL_FOUNDATIONS/axioms/registry.yaml'],
            'runtime_binding': None,
            'notes': 'Frozen foundation axiom from the standalone CIEL Foundations sector.'
        })

    const_tag_map = {
        'I0': ['type:constant','domain:foundations','domain:omega','status:working_definition','role:information','role:phase','role:closure','layer:foundations','bind:registry','math:topology'],
        'Lambda0': ['type:constant','domain:foundations','domain:omega','status:hypothesis','role:cosmology','role:curvature','layer:foundations','bind:registry','math:lagrangian','sector:cosmology'],
        'tau_i': ['type:constant','domain:foundations','domain:metatime','status:hypothesis','role:spectrum','role:transport','layer:foundations','bind:registry','math:spectrum','sector:neutrino'],
        'kappa': ['type:constant','domain:foundations','domain:metatime','status:hypothesis','role:coupling','layer:foundations','bind:registry','math:topology'],
    }
    for c in constants_reg['constants']:
        cards.append({
            'stable_id': f"GLOSS-{c['id']}",
            'canonical_id': f"constant.{slug(c['symbol'])}",
            'symbol': c['symbol'],
            'name': c['name'],
            'card_type': 'constant',
            'class': 'constant',
            'subclass': None,
            'status': c['status'],
            'certainty_scope': 'canonical_working_definition' if c['symbol'] == 'I0' else 'registry_working_hypothesis',
            'formula': c.get('exact_form') or None,
            'units': c.get('dimension', 'unknown'),
            'value': c.get('exact_form') or None,
            'numeric_value': None,
            'description': c['name'],
            'tags': const_tag_map.get(c['symbol'], ['type:constant','domain:foundations','status:hypothesis','bind:registry']),
            'relational_couplings': [],
            'cross_refs': [f"systems/CIEL_FOUNDATIONS/{c['folder']}"],
            'source_paths': ['systems/CIEL_FOUNDATIONS/constants/registry.yaml', f"systems/CIEL_FOUNDATIONS/{c['folder']}README.md"],
            'runtime_binding': None,
            'notes': 'Status taken from the foundations constants registry.'
        })

    cards.extend([
        {
            'stable_id':'GLOSS-SPACE-PROJECTIVE-CPN','canonical_id':'space.projective.cpn','symbol':'CP^n','name':'Projective State Space','card_type':'space','class':'space','subclass':'projective',
            'status':'research_note','certainty_scope':'active_repo_formalism','formula':'[psi] in CP^n ; psi^dagger psi = 1','units':'n/a','value':None,'numeric_value':None,
            'description':'Current minimal state-space used for non-arbitrary holonomy closure derivations.',
            'tags':['type:space','type:formalism','domain:foundations','status:research_note','role:state','role:phase','layer:foundations','bind:derived','math:hilbert','math:projective'],
            'relational_couplings':['couples_to:A_mu','couples_to:F_munu','stabilizes:closure'],
            'cross_refs':['docs/concepts/NON_ARBITRARY_HOLONOMY_CLOSURE_B1_B2.md','GLOSS-AX-001'],
            'source_paths':['docs/concepts/NON_ARBITRARY_HOLONOMY_CLOSURE_B1_B2.md'],
            'runtime_binding':None,
            'notes':'Derived from the current canonical research note; not yet frozen as a foundations axiom text.'
        },
        {
            'stable_id':'GLOSS-FIELD-PHASE-CONNECTION','canonical_id':'field.connection.a_mu','symbol':'A_mu','name':'Phase Connection','card_type':'formalism','class':'field','subclass':'connection',
            'status':'research_note','certainty_scope':'active_repo_formalism','formula':'D_mu psi = (partial_mu + i A_mu) psi','units':'phase connection / gauge field','value':None,'numeric_value':None,
            'description':'Minimal connection field carrying phase transport and holonomy in the non-arbitrary closure derivation.',
            'tags':['type:formalism','domain:foundations','status:research_note','role:phase','role:transport','role:holonomy','layer:foundations','bind:derived','math:connection'],
            'relational_couplings':['couples_to:CP^n','couples_to:F_munu','constrains:Loop'],
            'cross_refs':['GLOSS-FIELD-CURVATURE','GLOSS-FUNCTIONAL-HOLONOMY-CLOSURE','GLOSS-TOPOLOGY-LOOP-BASE'],
            'source_paths':['docs/concepts/NON_ARBITRARY_HOLONOMY_CLOSURE_B1_B2.md'],
            'runtime_binding':None,
            'notes':'Current minimal field variable for B1/B2 derivation.'
        },
        {
            'stable_id':'GLOSS-FIELD-CURVATURE','canonical_id':'field.curvature.f_munu','symbol':'F_munu','name':'Curvature Field','card_type':'formalism','class':'field','subclass':'curvature',
            'status':'research_note','certainty_scope':'active_repo_formalism','formula':'F_munu = partial_mu A_nu - partial_nu A_mu','units':'connection curvature','value':None,'numeric_value':None,
            'description':'Curvature induced by the phase connection; enters the minimal Lagrangian and closure dynamics.',
            'tags':['type:formalism','domain:foundations','status:research_note','role:curvature','role:holonomy','layer:foundations','bind:derived','math:curvature'],
            'relational_couplings':['couples_to:A_mu','projects_to:TriangleLoopPhase'],
            'cross_refs':['GLOSS-FIELD-PHASE-CONNECTION','GLOSS-FORMALISM-HOLONOMY-LAGRANGIAN'],
            'source_paths':['docs/concepts/NON_ARBITRARY_HOLONOMY_CLOSURE_B1_B2.md'],
            'runtime_binding':None,
            'notes':'Used in the minimal B-branch Lagrangian.'
        },
        {
            'stable_id':'GLOSS-FORMALISM-HOLONOMY-LAGRANGIAN','canonical_id':'formalism.holonomy.closure.lagrangian','symbol':'L_HC','name':'Holonomy Closure Lagrangian','card_type':'formalism','class':'formalism','subclass':'lagrangian',
            'status':'research_note','certainty_scope':'active_repo_formalism','formula':'(D_mu psi)^dagger D^mu psi - lambda(psi^dagger psi-1) - (1/4g^2)F^2 - mu sum_a(oint A - chi)^2','units':'lagrangian density','value':None,'numeric_value':None,
            'description':'Current minimal non-arbitrary Lagrangian used to derive B1 and B2 branches from state, connection, curvature, and closure classes.',
            'tags':['type:formalism','domain:foundations','domain:metatime','status:research_note','role:closure','role:holonomy','role:transport','layer:foundations','bind:derived','math:lagrangian','sector:neutrino'],
            'relational_couplings':['couples_to:A_mu','couples_to:F_munu','couples_to:CP^n','couples_to:ClosureClass'],
            'cross_refs':['GLOSS-FIELD-PHASE-CONNECTION','GLOSS-FIELD-CURVATURE','GLOSS-CONSTRAINT-CLOSURE-CLASS','GLOSS-EFFECT-B1-SPINOR-GAP','GLOSS-EFFECT-B2-BARGMANN-PHASE'],
            'source_paths':['docs/concepts/NON_ARBITRARY_HOLONOMY_CLOSURE_B1_B2.md'],
            'runtime_binding':None,
            'notes':'Research note formalism; next step is promotion into frozen derivation text and code solver.'
        },
        {
            'stable_id':'GLOSS-CONSTRAINT-CLOSURE-CLASS','canonical_id':'constraint.closure.chi_a','symbol':'chi_a','name':'Admissible Closure Class','card_type':'constraint','class':'constraint','subclass':'closure_class',
            'status':'research_note','certainty_scope':'active_repo_formalism','formula':'chi_a in {2*pi*nu_a, pi(2*nu_a+1)}','units':'radians','value':None,'numeric_value':None,
            'description':'Allowed bosonic or spinor holonomy class imposed on each representative loop.',
            'tags':['type:constraint','domain:foundations','status:research_note','role:closure','role:spin','layer:foundations','bind:derived','math:topology'],
            'relational_couplings':['constrains:A_mu','constrains:Loop','projects_to:SpinorClosure'],
            'cross_refs':['GLOSS-FORMALISM-HOLONOMY-LAGRANGIAN','GLOSS-CONSTRAINT-SPINOR-CLOSURE'],
            'source_paths':['docs/concepts/NON_ARBITRARY_HOLONOMY_CLOSURE_B1_B2.md'],
            'runtime_binding':None,
            'notes':'Closure selector for the minimal B-branch derivation.'
        },
        {
            'stable_id':'GLOSS-EFFECT-B1-SPINOR-GAP','canonical_id':'effect.b1.spinor_gap','symbol':'E0_spinor','name':'B1 Minimal Spinor Gap','card_type':'effect','class':'observable','subclass':'toy_gap',
            'status':'measured','certainty_scope':'repo_numeric_result','formula':'For n=0 spinor class, a*=1/2 and ground energy = 1/4','units':'dimensionless toy energy','value':'1/4','numeric_value':0.25,
            'description':'Measured toy result from the single-loop branch: spinor closure leaves a nonzero minimal spectral gap after defect minimization.',
            'tags':['type:effect','type:observable','domain:foundations','domain:metatime','status:measured','role:closure','role:spin','layer:research','bind:derived','math:topology','sector:neutrino'],
            'relational_couplings':['depends_on:chi_a','depends_on:A_theta','supports:SpinorClosure'],
            'cross_refs':['GLOSS-CONSTRAINT-CLOSURE-CLASS','GLOSS-CONSTRAINT-SPINOR-CLOSURE','GLOSS-FORMALISM-HOLONOMY-LAGRANGIAN'],
            'source_paths':['research/holonomy_closure_b1_b2/results.json','docs/concepts/NON_ARBITRARY_HOLONOMY_CLOSURE_B1_B2.md'],
            'runtime_binding':None,
            'notes':'Numerically trivial but canonically recorded toy measurement.'
        },
        {
            'stable_id':'GLOSS-EFFECT-B2-BARGMANN-PHASE','canonical_id':'effect.b2.bargmann_phase','symbol':'Arg(B_123)','name':'B2 Triangle Bargmann Phase','card_type':'effect','class':'observable','subclass':'loop_phase',
            'status':'measured','certainty_scope':'repo_numeric_result','formula':'Arg(B_123) = Arg(<psi1|psi2><psi2|psi3><psi3|psi1>)','units':'radians','value':'-0.266443107496 rad ; -15.266066 deg','numeric_value':-0.26644310749634853,
            'description':'First canonical repo CP-like loop observable obtained from current geometry seeds without inserting an external fitted phase.',
            'tags':['type:effect','type:observable','domain:foundations','domain:metatime','status:measured','role:cp','role:holonomy','role:chirality','layer:research','bind:derived','math:spectrum','math:projective','sector:neutrino'],
            'relational_couplings':['depends_on:tau_i','depends_on:phi_i','projects_to:TriangleLoopPhase'],
            'cross_refs':['GLOSS-OBSERVABLE-CP-TRIANGLE-LOOP-PHASE','GLOSS-OBSERVABLE-TRANSPORT-SPECTRUM','reports/global_orbital_coherence_pass/real_geometry.json'],
            'source_paths':['research/holonomy_closure_b1_b2/results.json','docs/concepts/NON_ARBITRARY_HOLONOMY_CLOSURE_B1_B2.md','reports/global_orbital_coherence_pass/real_geometry.json'],
            'runtime_binding':None,
            'notes':'Measured on canonical triad (constraints, memory, runtime).'
        },
    ])

    status_map = {
        'constraint.euler': ('operational','runtime_bound_canonical_record'),
        'operator.closure.core': ('operational','runtime_bound_canonical_record'),
        'channel.holonomy.white_threads': ('operational','runtime_bound_canonical_record'),
        'trajectory.cqcl.compiler': ('operational','runtime_bound_canonical_record'),
    }
    card_type_overrides = {
        'operator.information.i0':'operator', 'operator.lambda.lambda0':'operator', 'operator.resonance.core':'operator', 'constraint.euler':'constraint', 'operator.closure.core':'operator', 'channel.holonomy.white_threads':'coupling', 'functional.holonomy.closure':'coupling', 'observable.transport.spectrum':'observable', 'observable.cp.triangle_loop_phase':'observable', 'seed.midpoint.twin_prime':'seed', 'seed.collatz.base':'seed', 'seed.zeta.base':'seed', 'attractor.core.anu':'attractor', 'attractor.seed.marduk':'attractor', 'phase.scalar.base':'state', 'state.coherence.base':'state', 'state.holonomy.emotion':'state', 'memory.trace.base':'memory', 'topology.winding.base':'topology', 'topology.loop.base':'topology', 'constraint.spinor.closure':'constraint', 'trajectory.cqcl.compiler':'formalism', 'state.symbolic.vocabulary':'formalism',
    }
    symbol_tags = {
        'TriangleLoopPhase':['role:cp','sector:neutrino'],
        'TransportSpectrum':['role:spectrum','role:transport','sector:neutrino'],
        'Lambda0':['sector:cosmology','role:curvature'],
        'MemoryTrace':['sector:memory','role:memory'],
        'CQCL':['domain:semantics','role:compiler'],
        'WhiteThreads':['role:holonomy','role:coupling'],
        'EulerConstraint':['role:closure','role:identity'],
        'SpinorClosure':['role:spin','role:closure'],
        'Winding':['role:identity','role:topology'],
        'Loop':['role:identity','role:memory','role:closure'],
        'Coherence':['role:coherence'],
        'Phase':['role:phase'],
        'I0':['role:information','role:closure','role:phase'],
    }
    for rec in vocab['records']:
        cid = rec['canonical_id']
        status, scope = status_map.get(cid, ('canonical_record','canonical_ontology_record'))
        const_match = next((c for c in constants_reg['constants'] if c['symbol'] == rec['symbol'] or (rec['symbol'] == 'TransportSpectrum' and c['symbol'] == 'tau_i')), None)
        if const_match and rec['symbol'] in {'I0','Lambda0'}:
            status = 'working_definition' if rec['symbol'] == 'I0' else 'hypothesis'
            scope = 'canonical_working_definition' if rec['symbol'] == 'I0' else 'registry_working_hypothesis'
        tags = [f"type:{card_type_overrides.get(cid, rec['class'])}", 'domain:omega', f"status:{status}", f"role:{slug(rec.get('semantics', {}).get('role', 'formal').split()[0])}", f"layer:{'runtime' if rec.get('runtime_binding') else 'ontology'}", f"bind:{'runtime' if rec.get('runtime_binding') and rec.get('runtime_binding', {}).get('mode') != 'deferred' else 'registry'}"]
        if rec['symbol'] in {'I0','Lambda0','TransportSpectrum','TriangleLoopPhase','EulerConstraint','SpinorClosure','WhiteThreads','HolonomyClosureFunctional','Winding','Loop'}:
            tags.append('domain:foundations')
        if rec['symbol'] in {'TransportSpectrum','TriangleLoopPhase','WhiteThreads','TwinPrimeMidpoint','CollatzSeed','ZetaSeed'}:
            tags.append('domain:metatime')
        formal = rec.get('operator', {}).get('formal') or rec.get('semantics', {}).get('invariant')
        text = (formal or '') + ' ' + (rec.get('semantics', {}).get('phase_behavior') or '')
        for key, tag in [('hilbert','math:hilbert'),('phase','math:topology'),('arg','math:spectrum'),('spec','math:spectrum'),('integral','math:topology'),('closure','math:topology'),('transport','math:connection')]:
            if key in text.lower() and tag not in tags:
                tags.append(tag)
        tags.extend(symbol_tags.get(rec['symbol'], []))
        tags = list(dict.fromkeys(tags))
        cards.append({
            'stable_id': 'GLOSS-' + cid.replace('.', '-').replace('_', '-').upper(),
            'canonical_id': cid,
            'symbol': rec['symbol'],
            'name': rec['aliases'][0] if rec.get('aliases') else rec['symbol'],
            'card_type': card_type_overrides.get(cid, rec['class']),
            'class': rec['class'],
            'subclass': rec.get('subclass'),
            'status': status,
            'certainty_scope': scope,
            'formula': formal,
            'units': const_match.get('dimension') if const_match else 'see card / symbolic',
            'value': const_match.get('exact_form') if const_match and const_match.get('exact_form') else None,
            'numeric_value': None,
            'description': rec.get('semantics', {}).get('role', ''),
            'tags': tags,
            'relational_couplings': [f"{rel}:{','.join(targets)}" for rel, targets in rec.get('relations', {}).items()],
            'cross_refs': list(dict.fromkeys((rec.get('targets') or []) + [*rec.get('relations', {}).keys()])),
            'source_paths': ['systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary.yaml'],
            'runtime_binding': rec.get('runtime_binding'),
            'notes': rec.get('semantics', {}).get('phase_behavior', '')
        })

    uniq, seen = [], set()
    for c in cards:
        if c['stable_id'] in seen:
            continue
        seen.add(c['stable_id'])
        uniq.append(c)
    cards = uniq

    for c in cards:
        c['card_path'] = f"systems/CIEL_FOUNDATIONS/definitions/cards/{c['stable_id']}-{slug(c['symbol'])}.md"
        c['source_of_truth'] = 'yaml+markdown' if c['status'] != 'measured' else 'json+markdown'

    readme_lines = ['# Glossary Cards','','Canonical glossary cards: one formal object per card, with tags, IDs, status, formula, relational couplings, and cross-references.','']
    for c in sorted(cards, key=lambda x: (x['card_type'], x['symbol'].lower())):
        lines = [f"# {c['symbol']} - {c['name']}", '', '| field | value |', '|---|---|', f"| stable_id | `{c['stable_id']}` |", f"| canonical_id | `{c['canonical_id']}` |", f"| card_type | `{c['card_type']}` |", f"| class | `{c['class']}` |", f"| subclass | `{c['subclass'] or ''}` |", f"| status | `{c['status']}` |", f"| certainty_scope | `{c['certainty_scope']}` |", f"| units | `{c['units']}` |", f"| value | `{c['value'] or ''}` |"]
        if c['numeric_value'] is not None:
            lines.append(f"| numeric_value | `{c['numeric_value']}` |")
        lines += ['', '## Description', c['description'] or 'No description yet.', '', '## Formal definition', '```text', c['formula'] or 'n/a', '```', '', '## Tags', ', '.join(f'`{t}`' for t in c['tags']) if c['tags'] else 'none', '', '## Relational couplings']
        if c['relational_couplings']:
            lines += ['| relation | targets |', '|---|---|']
            for rc in c['relational_couplings']:
                rel, targets = rc.split(':', 1)
                lines.append(f'| `{rel}` | `{targets}` |')
        else:
            lines.append('No explicit relational couplings registered yet.')
        lines += ['', '## Cross references']
        lines.extend([f'- `{cr}`' for cr in c['cross_refs']] if c['cross_refs'] else ['- none'])
        lines += ['', '## Source-of-truth anchors']
        lines.extend([f'- `{sp}`' for sp in c['source_paths']])
        if c['runtime_binding']:
            lines += ['', '## Runtime binding', '```yaml', yaml.safe_dump(c['runtime_binding'], sort_keys=False).strip(), '```']
        if c['notes']:
            lines += ['', '## Notes', c['notes']]
        (repo / c['card_path']).write_text('\n'.join(lines) + '\n')
        readme_lines.append(f"- [{c['symbol']}](./{Path(c['card_path']).name}) - `{c['stable_id']}`")
    (cards_dir / 'README.md').write_text('\n'.join(readme_lines) + '\n')

    registry = {'schema_version': '1.0', 'description': 'Canonical glossary registry: one formal object per card with stable ID, tags, crossrefs, and evidence anchors.', 'cards': [], 'groups': {'axioms':[], 'spaces':[], 'formalism':[], 'constants':[], 'operators':[], 'constraints':[], 'couplings':[], 'observables':[], 'states':[], 'topology':[], 'seeds':[], 'attractors':[], 'effects':[]}}
    group_map = {'axiom':'axioms','space':'spaces','formalism':'formalism','constant':'constants','operator':'operators','constraint':'constraints','coupling':'couplings','observable':'observables','state':'states','memory':'states','topology':'topology','seed':'seeds','attractor':'attractors','effect':'effects'}
    for c in sorted(cards, key=lambda x: x['stable_id']):
        entry = {k: c[k] for k in ['stable_id','canonical_id','symbol','name','card_type','class','subclass','status','certainty_scope','formula','units','value','numeric_value','tags','relational_couplings','cross_refs','source_paths','card_path','source_of_truth']}
        if c['runtime_binding']:
            entry['runtime_binding'] = c['runtime_binding']
        registry['cards'].append(entry)
        grp = group_map.get(c['card_type'])
        if grp:
            registry['groups'][grp].append(c['stable_id'])
    (found / 'definitions/registry.yaml').write_text(yaml.safe_dump(registry, sort_keys=False, allow_unicode=True))

    rows = [{'stable_id': c['stable_id'], 'canonical_id': c['canonical_id'], 'symbol': c['symbol'], 'name': c['name'], 'type': c['card_type'], 'status': c['status'], 'certainty_scope': c['certainty_scope'], 'units': c['units'], 'value': c['value'] or '', 'numeric_value': '' if c['numeric_value'] is None else c['numeric_value'], 'relations': ' ; '.join(c['relational_couplings']), 'tags': ' | '.join(c['tags'])} for c in sorted(cards, key=lambda x: (x['card_type'], x['symbol'].lower()))]
    with (found / 'definitions/tables/glossary_master.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader(); writer.writerows(rows)
    table_lines = ['# Glossary Master Table','','| stable_id | symbol | type | status | units | value | relations |','|---|---|---|---|---|---|---|']
    for r in rows:
        table_lines.append(f"| `{r['stable_id']}` | `{r['symbol']}` | `{r['type']}` | `{r['status']}` | `{r['units']}` | `{r['value']}` | `{r['relations'][:120]}` |")
    (found / 'definitions/tables/GLOSSARY_MASTER_TABLE.md').write_text('\n'.join(table_lines) + '\n')

    con = sqlite3.connect(generated_dir / 'ciel_semantic_glossary.db')
    cur = con.cursor()
    cur.executescript('''
DROP TABLE IF EXISTS cards;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS relations;
DROP TABLE IF EXISTS crossrefs;
DROP TABLE IF EXISTS runtime_bindings;
DROP TABLE IF EXISTS source_paths;
CREATE TABLE cards (stable_id TEXT PRIMARY KEY, canonical_id TEXT, symbol TEXT, name TEXT, card_type TEXT, class TEXT, subclass TEXT, status TEXT, certainty_scope TEXT, formula TEXT, units TEXT, value TEXT, numeric_value REAL, card_path TEXT, source_of_truth TEXT);
CREATE TABLE tags (stable_id TEXT, tag TEXT);
CREATE TABLE relations (stable_id TEXT, relation TEXT, target TEXT);
CREATE TABLE crossrefs (stable_id TEXT, crossref TEXT);
CREATE TABLE runtime_bindings (stable_id TEXT, module TEXT, object TEXT, field TEXT, function TEXT, mode TEXT);
CREATE TABLE source_paths (stable_id TEXT, source_path TEXT);
''')
    for c in cards:
        cur.execute('INSERT INTO cards VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (c['stable_id'], c['canonical_id'], c['symbol'], c['name'], c['card_type'], c['class'], c['subclass'], c['status'], c['certainty_scope'], c['formula'], c['units'], c['value'], c['numeric_value'], c['card_path'], c['source_of_truth']))
        cur.executemany('INSERT INTO tags VALUES (?,?)', [(c['stable_id'], t) for t in c['tags']])
        rel_rows = []
        for rc in c['relational_couplings']:
            rel, target = rc.split(':', 1)
            for tgt in target.split(','):
                rel_rows.append((c['stable_id'], rel, tgt))
        cur.executemany('INSERT INTO relations VALUES (?,?,?)', rel_rows)
        cur.executemany('INSERT INTO crossrefs VALUES (?,?)', [(c['stable_id'], cr) for cr in c['cross_refs']])
        rb = c['runtime_binding'] or {}
        if rb:
            cur.execute('INSERT INTO runtime_bindings VALUES (?,?,?,?,?,?)', (c['stable_id'], rb.get('module'), rb.get('object'), rb.get('field'), rb.get('function'), rb.get('mode')))
        cur.executemany('INSERT INTO source_paths VALUES (?,?)', [(c['stable_id'], sp) for sp in c['source_paths']])
    con.commit()

    card_type_counts = Counter(c['card_type'] for c in cards)
    status_counts = Counter(c['status'] for c in cards)
    class_counts = Counter(c['class'] for c in cards)
    tag_counts = Counter(t for c in cards for t in c['tags'])
    outdeg, indeg = Counter(), Counter()
    edge_count = 0
    for c in cards:
        for rc in c['relational_couplings']:
            rel, target = rc.split(':', 1)
            for tgt in target.split(','):
                outdeg[c['stable_id']] += 1
                indeg[tgt] += 1
                edge_count += 1
    co = Counter()
    for c in cards:
        ts = sorted(set(c['tags']))
        for i in range(len(ts)):
            for j in range(i + 1, len(ts)):
                co[(ts[i], ts[j])] += 1
    runtime_bound = sum(1 for c in cards if c['runtime_binding'] and c['runtime_binding'].get('mode') != 'deferred')
    ledger_stats = []
    for lp in [repo / 'systems/CIEL_OMEGA_COMPLETE_SYSTEM/CIEL_MEMORY_SYSTEM/TSM/ledger/memory_ledger.db', repo / 'systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/CIEL_MEMORY_SYSTEM/TSM/ledger/memory_ledger.db']:
        if lp.exists():
            con2 = sqlite3.connect(lp)
            cnt = con2.execute('SELECT COUNT(*) FROM memories').fetchone()[0]
            ledger_stats.append({'path': str(lp.relative_to(repo)), 'rows': cnt})
            con2.close()
    stats = {'generated_at': '2026-03-24', 'total_cards': len(cards), 'card_type_counts': dict(card_type_counts), 'class_counts': dict(class_counts), 'status_counts': dict(status_counts), 'runtime_binding_coverage': {'runtime_bound_cards': runtime_bound, 'coverage_fraction': runtime_bound / len(cards)}, 'relation_graph': {'edge_count': edge_count, 'top_out_degree': outdeg.most_common(10), 'top_in_degree_targets': indeg.most_common(10)}, 'tag_counts_top20': tag_counts.most_common(20), 'tag_correlations_top20': [[a,b,n] for (a,b),n in co.most_common(20)], 'semantic_memory_ledgers': ledger_stats, 'semantic_glossary_db_tables': [r[0] for r in cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()]}
    (generated_dir / 'ciel_semantic_glossary_stats.json').write_text(json.dumps(stats, indent=2))
    report = ['# Canonical Glossary + Semantic DB Report','', '## Summary', f'- total cards: **{len(cards)}**', f'- runtime-bound cards: **{runtime_bound}** ({runtime_bound/len(cards):.1%})', f'- relation edges: **{edge_count}**', '', '## Card type counts']
    report.extend([f'- `{k}`: {v}' for k, v in card_type_counts.items()])
    report += ['', '## Status counts']
    report.extend([f'- `{k}`: {v}' for k, v in status_counts.items()])
    report += ['', '## Top relation hubs']
    report.extend([f'- `{sid}`: out-degree {n}' for sid, n in outdeg.most_common(10)])
    report += ['', '## Top tag co-occurrences']
    report.extend([f'- `{a}` + `{b}`: {n}' for (a, b), n in co.most_common(15)])
    report += ['', '## Semantic ledger status']
    report.extend([f"- `{row['path']}`: rows={row['rows']}" for row in ledger_stats])
    report += ['', '## Interpretation boundary', '- The glossary DB is generated from canonical YAML/Markdown/JSON sources and is **not** itself source of truth.', '- The Omega memory ledger databases currently contain **0 semantic memory rows**, so glossary correlations were computed from the canonical semantic graph rather than live memory traces.', '- Cards use stable IDs so each value/operator/effect can be referenced uniformly across foundations, reports, runtime vocabulary, and future LaTeX/publication layers.']
    (generated_dir / 'ciel_semantic_glossary_stats.md').write_text('\n'.join(report) + '\n')
    (reports_dir / 'GLOSSARY_CANONICALIZATION_2026-03-24.md').write_text('\n'.join(report) + '\n')

    (found / 'definitions/README.md').write_text(textwrap.dedent('''
# Definitions

This sector now contains canonical glossary cards.

## Rule
One formal object per card.
Each card must have:
- stable ID
- canonical ID
- tags
- epistemic status
- formal definition
- relational couplings
- cross-references
- source-of-truth anchors

## Main artifacts
- `registry.yaml` - machine-readable glossary registry
- `cards/` - one card per formal object
- `tables/GLOSSARY_MASTER_TABLE.md` - compact search table
- `tables/glossary_master.csv` - machine-readable compact table
- `tags.yaml` - tag taxonomy
''').strip() + '\n')
    con.close()
    return stats


def main() -> None:
    repo = Path(__file__).resolve().parents[5]
    build(repo)


if __name__ == '__main__':
    main()
