# Routinen Uebersicht

Stand: 2026-02-06

## apps/api/app/__init__.py
- Keine Routinen (Datei leer).

## apps/api/app/main.py
- `health_check()`
- `list_themes()`
- `list_milestones()`
- `get_milestone(milestone_id)`
- `list_tasks(milestone=None)`
- `get_operatorenliste()`

## apps/api/app/data_loader.py
- `_repo_root()`
- `_data_dir()`
- `load_json(name)`
- `load_text(relative_path)`

## apps/tools/generate_information_docs.py
- `first_paragraph(text)`
- `collect_defs(node_list)`
- `analyze_py(path)`
- `analyze_text(path)`
- `unique_out_path(base)`
- `make_md_for_file(src_path, rel_path)`
- `main()`

## src/utils/version_manager.py
- Keine Routinen (Datei leer).

## src/utils/struktogramm_helper.py

### Klassen und Methoden
- `StruktogrammElement`
  - `__post_init__()`
- `StruktogrammValidator`
  - `validate_line(line)`
  - `validate_struktogramm(lines)`
- `StruktogrammRenderer`
  - `render_box(content, width=55)`
  - `render_branch(condition, j_content, n_content, width=55)`
  - `render_loop(condition, body, width=55)`
- `StruktogrammBuilder`
  - `__init__()`
  - `_indent()`
  - `deklaration(variable, datentyp=None)`
  - `initialisierung(variable, wert)`
  - `dekl_init(variable, wert, datentyp=None)`
  - `zuweisung(variable, wert)`
  - `einlesen(variable, datentyp=None)`
  - `ausgabe(inhalt)`
  - `rueckgabe(wert)`
  - `aufruf(methode, parameter="")`
  - `wenn_start(bedingung)`
  - `sonst()`
  - `wenn_ende()`
  - `wiederhole_solange_start(bedingung)`
  - `schleife_ende()`
  - `zaehle_start(variable, start, ende, schrittweite="1")`
  - `wiederhole_von_start(variable, start, bedingung, schrittweite="1")`
  - `build()`
  - `validate()`

### Funktionen
- `pattern_array_durchlaufen(array_name, index_var="i")`
- `pattern_summe_berechnen(array_name, summe_var="summe")`
- `pattern_maximum_finden(array_name)`
- `pattern_lineare_suche(array_name, such_var="suchWert")`
- `load_struktogramm_from_file(filepath)`
- `save_struktogramm_to_file(filepath, content)`
- `print_validation_results(errors)`

## src/utils/elearning_manager.py

### Klassen und Methoden
- `ELearningMetadata`
  - `to_filename(content_type)`
  - `to_frontmatter()`
- `ELearningAufgabe`
  - `to_markdown()`
- `ELearningInformation`
  - `to_markdown()`
- `ELearningLoesung`
  - `to_markdown()`
- `ELearningManager`
  - `__init__(base_path="/workspaces/python-algorithmen-datenstrukturen")`
  - `_get_target_path(metadata, content_type)`
  - `save_aufgabe(aufgabe)`
  - `save_information(info)`
  - `save_loesung(loesung)`
  - `generate_index(content_type, level=None)`
  - `generate_all_indices()`
  - `validate_content(file_path)`

### Funktionen
- `create_aufgabe_quick(titel, level, kategorie, nummer, problemstellung, autor="Unbekannt", struktogramm=None)`
- `create_information_quick(titel, level, kategorie, nummer, einfuehrung, inhalt, autor="Unbekannt")`
- `create_loesung_quick(titel, level, kategorie, nummer, loesungsansatz, python_code, autor="Unbekannt", struktogramm=None)`

## src/utils/pruefungen_namenskonvention.py

### Funktionen
- `ist_konformer_dateiname(dateiname)`
- `analysiere_pruefungsdatei(datei)`
- `normalisiere_pruefungsdateien(basis_verzeichnis, dry_run=True)`

### Dataklassen
- `PruefungsDateiBefund`
- `Umbenennung`
- `NormalisierungsErgebnis`

## apps/tools/pruefungen_dateinamen_manager.py
- `_repo_root()`
- `_parse_args()`
- `main()`

## src/niveau/ka_template/KA02_INF_BG13_2025_2025_lsg.py
- `ermittleErgebnis()`
- `ermittleSatzAusArray()`
- `ermittleFrageAusArray()`
- `ermittleRechnungsbetrag()`
- `ermittleRabattUndRechnungsbetrag()`
- `ermittleBonus()`
- `sortiereMitBubbleSort()`
