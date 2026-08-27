# 🛡️ Security Notes & Known Vulnerabilities

**Last Updated:** 18.02.2026  
**Phase:** 1 (Repository Setup)

---

## 📋 Executive Summary

Das Projekt hat **8 npm vulnerabilities** (3 low, 5 moderate severity). 

**Risk Assessment für Phase 1:** ✅ **LOW**
- Kein Production-Code vorhanden
- Nur DevDependencies & nicht-kritische Libraries

**Decision:** Dokumentieren, nicht fixen (Option B)  
**Reason:** Breaking Changes in Phase 1 würden Fortschritt verlangsamen

---

## 🔴 Kritische Vulnerabilities

### 1. **mxgraph - XSS in setTooltips Function**

**Severity:** 🟠 Moderate  
**ID:** GHSA-j4rv-pr9g-q8jv  

**Beschreibung:**
```
Die mxgraph Library hat eine Cross-Site Scripting (XSS) Lücke
in der setTooltips() Funktion. Ein Angreifer könnte bösartigen
JavaScript-Code in Tooltips injizieren.
```

**Status:** ❌ **NO FIX AVAILABLE**
- mxGraph ist nicht mehr aktiv gepflegt
- Letzter Release: 2024
- Sicherheits-Updates sind unwahrscheinlich

**Unser Umgang damit:**
- ⚠️ Diese Library ist KERN-Dependency für Draw.io Integration
- ✅ Phase 1: Akzeptabel (noch kein Code mit setTooltips)
- 🔄 Phase 2: **MUSS evaluiert werden**
  - Option A: Tolerate das Risiko (wenn nicht kritisch)
  - Option B: Auf mxgraph Fork wechseln (z.B. `@masturflow/mxgraph`)
  - Option C: Alternative Graphics Library evaluieren

**Action Items:**
```
- [ ] Phase 2: User Input in setTooltips sanitizen (wenn genutzt)
- [ ] Phase 2: Alternatives wie graphlib / yFiles evaluieren
- [ ] Phase 3: Code Review für XSS-Anfälligkeit
```

---

### 2. **ajv - ReDoS Vulnerability**

**Severity:** 🟠 Moderate  
**ID:** GHSA-2g4f-4pwh-qvx6  

**Beschreibung:**
```
ajv hat eine ReDoS-Lücke (Regular Expression Denial of Service).
Ein Angreifer könnte spezielle Input-Strings nur Validierung
zum Absturz bringen (DoS-Attacke).
```

**Abhängigkeitskette:**
```
eslint 8.56.0
  └─ table 3.7.10 - 6.0.7
      └─ ajv-keywords 2.1.1 - 4.0.1
          └─ ajv < 8.18.0 (VULNERABLE)
```

**Verfügbarer Fix:**
```
npm audit fix --force
→ würde eslint auf 10.0.0 upgraden (Breaking Change!)
→ ESLint Config müsste überarbeitet werden
```

**Unser Umgang damit:**
- ⚠️ Nur in DevDependencies (nicht in Production)
- ✅ Phase 1: Akzeptabel (ESLint noch nicht konfiguriert)
- 🔄 Phase 2: Wenn ESLint Setup beginnt, dann upgraden

**Action Items:**
```
- [ ] Phase 2: ESLint Config schreiben
- [ ] Phase 2: Gleichzeitig auf eslint 10.0.0 + ajv 8.18.0+ upgraden
- [ ] Phase 2: npm audit erneut laufen
```

---

### 3. **tmp - Symbolic Link Vulnerability**

**Severity:** 🟠 Moderate  
**ID:** GHSA-52f5-9888-hmc6  

**Beschreibung:**
```
Die tmp Library hat eine Symbolic Link Lücke. Ein Angreifer
könnte auf sensitive Dateien zugreifen über Symlinks in
temporären Verzeichnissen.
```

**Abhängigkeitskette:**
```
eslint 8.56.0
  └─ inquirer 3.0.0 - 9.3.7
      └─ external-editor >=1.1.1
          └─ tmp <=0.2.3 (VULNERABLE)
```

**Verfügbarer Fix:**
```
npm audit fix --force
→ würde inquirer upgraden (Breaking Change!)
→ Könnte CLI-Prompts beeinflussen
```

**Unser Umgang damit:**
- ⚠️ Nur in DevDependencies + nur CLI-basiert
- ✅ Phase 1: Akzeptabel (kein Interactive CLI noch nicht vorhanden)
- 🔄 Phase 2: Bei Bedarf upgraden

**Action Items:**
```
- [ ] Phase 2: Wenn tmp-Funktionalität genutzt wird, updaten
- [ ] Phase 2: npm audit fix --force + Testing durchführen
```

---

## 📊 Vulnerability Overview Table

| Library | Severity | Issue | Available Fix | Phase 1 Risk | Action |
|---------|----------|-------|----------------|-------------|--------|
| **mxgraph** | 🟠 Mod | XSS | ❌ None | LOW | Evaluate Phase 2 |
| **ajv** | 🟠 Mod | ReDoS | ✅ Yes* | LOW | Defer to Phase 2 |
| **tmp** | 🟠 Mod | Symlink | ✅ Yes* | LOW | Defer to Phase 2 |
| 5 Low | 🟢 Low | Various | ✅ Yes* | VERY LOW | Ignore for now |

*Breaking Changes in fixes

---

## 🔄 Timeline für Fixes

### Phase 1 (JETZT)
- ✅ **Action:** Dokumentieren (diese Datei)
- ✅ **Decision:** Nicht fixen
- ✅ **Reason:** Würde Momentum killen

### Phase 2 (Nächste Woche)
- 🔄 **Action:** mxgraph-Alternativen evaluieren
- 🔄 **Decision:** Upgrade-Plan für eslint 10.0.0
- 🔄 **Reason:** Wenn echter Code kommt, dann sauberes Setup

### Phase 3 (2-3 Wochen)
- 🔄 **Action:** npm audit fix anwenden + full testing
- 🔄 **Decision:** Finales Security Review vor V1 Release
- 🔄 **Reason:** Vor öffentlicher Nutzung (npm publishing)

---

## 🛠️ Wie man Vulnerabilities monitored

### Regelmäßig Überprüfen:
```bash
# Manuell:
npm audit

# Mit Details:
npm audit --full

# JSON für Automation:
npm audit --json > audit-report.json
```

### CI/CD Integration (später):
```yaml
# Im GitHub Actions Workflow
- name: Security Audit
  run: |
    npm audit --audit-level=moderate
    # Fails if moderate+ vulnerabilities found
```

---

## 🔐 Best Practices für Phase 2+

1. **Regelmäßig `npm audit` laufen**
   - Nach jedem `npm install`
   - Vor jedem Commit zu main

2. **Vulnerability Response Prozess**
   ```
   Kritisch (Critical) → Fix sofort
   Hoch (High) → Fix in dieser Woche
   Moderat (Moderate) → Fix im nächsten Sprint
   Niedrig (Low) → Review & dokumentieren
   ```

3. **Dependabot nutzen** (GitHub Feature)
   - Erstellt automatisch PRs für Updates
   - Schreibt Security Alerts
   - Workflow: Review → Merge → Monitor

4. **npm publish rules**
   - Vor `npm publish`: `npm audit` muss = 0 sein
   - Exceptions müssen dokumentiert werden
   - README muss Sicherheits-Status erwähnen

---

## 📚 Referenzen

- **npm audit Docs:** https://docs.npmjs.com/cli/v9/commands/npm-audit
- **GitHub Security Advisories:** https://github.com/advisories
- **OWASP XSS Prevention:** https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
- **mxgraph Alternatives:**
  - graphlib (Uber)
  - yFiles (commercial)
  - jsPlumb (open source)

---

## 🎯 Summary für Team

**Stand:** 18.02.2026  
**Phase:** 1  
**Decision:** Option B - Dokumentieren, nicht fixen  
**Reason:** Pragmatisch für Early-Stage Development  
**Next Review:** Phase 2 Start  
**Owner:** Christine Janischek

---

**Zuletzt aktualisiert:** 18.02.2026 via npm audit

<!-- CUSTOM_LICENSE_NOTICE_START -->
## License

This repository is licensed under a custom license.

- Attribution required: Christine Janischek - https://emotionalspirit.de
- Non-commercial use only
- Use only within state school systems
- Any other use requires explicit prior written permission
<!-- CUSTOM_LICENSE_NOTICE_END -->
