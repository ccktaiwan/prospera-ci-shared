# SKILL-CORE｜ProsperaGen AI Execution Core
## Document Header
- Document Type: Codex
- Version: v1.0
- Status: Approved
- Owner: prospera-ci-shared/skills/
- Governing Authority: prospera-engineering-codex v1.0
- DNA Reference: 要素一～十（全部）
- Last Updated: 2026-05-19

---

## 1. 強制讀取規則

**每次任務開始前**：讀完本文件再執行。
**特定情境**：查 §6 → 讀對應完整 Skill → 再執行。
不讀直接執行 = Governance Breach → CI 自動 BLOCK。

---

## 2. 標準任務流程

```
[開始] → 讀 SKILL-CORE §6 → 讀對應 Skill → 執行
       → 每完成重要步驟 → Checkpoint (SKILL-06)
       → git commit 前 → Pre-flight (SKILL-04)
       → 新錯誤 → 補進 known_failures.md
```

---

## 3. 命名規則

```
目錄：全小寫    ✅ 00_governance  ❌ 00_GOVERNANCE
檔案：全大寫    ✅ README.md      ❌ readme.md
```

---

## 4. Commit Message 格式

```
[Phase][Layer] 動作: 描述 (為什麼) ≤ 72 字元
範例：[P3][L2] feat: add authority-matrix (enforce access boundary)
禁用：update / fix / change / misc / WIP
```

---

## 5. AI Header 必要欄位

```
Generated / Model / Phase / Layer / Target Repo / Governing Codex / Human-Reviewed
```

---

## 6. Skill 查閱表

| Skill | 觸發條件 | 完整文件 |
|-------|---------|----------|
| SKILL-01 | 任何 .yml 寫入或修改前 | SKILL-01.md |
| SKILL-02 | 任何目錄建立或 git mv 前 | SKILL-02.md |
| SKILL-03 | 任何 token/PAT/secret 操作前 | SKILL-03.md |
| SKILL-04 | 任何 git commit 前 | SKILL-04.md |
| SKILL-05 | 每次任務開始前 + 每個 Stage 完成後 | SKILL-05.md |
| SKILL-06 | 多步驟任務每完成一個重要步驟後 | SKILL-06.md |
| SKILL-07 | 任何文件提交前 | SKILL-07.md |
| SKILL-08 | 每個新機制或新引擎建立後 | SKILL-08.md |
| SKILL-09 | 任何 99_archive 救援或檔案遷移前 | SKILL-09.md |
| SKILL-10 | 任何新 repo 建立或 repo 封存前 | SKILL-10.md |

---

*v1.0 · 2026-05-19 · prospera-ci-shared/skills/ · Kevin Chang（張淳嘉）*
