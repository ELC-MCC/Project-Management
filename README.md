# ELC Project Management

Password-protected project tracker for the ELC team. Static HTML/CSS/JS, no backend. Data lives in `data.json` in this repo and is pushed from the browser with the Sync button.

Site: https://ELC-MCC.github.io/Project-Management/

---

## Login and roles

1. Enter the team password on the StatiCrypt screen. The page decrypts.
2. Pick a role.

| Role | Password | Can do |
|---|---|---|
| Member | none | View everything, change task status, set due date/time, edit notes, sync, export CSV |
| Officer | Officer password | Everything above plus projects, teams, add/edit/delete tasks |

Logout in the top right returns to the role screen without asking for the team password again.

---

## The screen

```
+--------------------------------------------------------------+
| PROJECTS      | PROJECT NAME         [+ Add Task] [Export CSV] |
|  progress bar | status chips | search | person filter         |
|               | TOTAL | DONE | ACTIVE | OVERDUE | DUE TODAY   |
| TEAMS         | #  TASK  STATUS  ASSIGNED  TEAM  DUE DATE/TIME |
|  members      | 1  ....  ....    ....      ....  ....          |
+--------------------------------------------------------------+
```

Left sidebar: every project with a gold progress bar, a done count, and a red overdue count. Click one to load its sheet.

Teams sit under the projects, scoped to the selected project. **Attach** links a team that already exists to the current project, so a team does not have to be created twice.

The stats strip counts the selected project's active tasks: total, done, active, overdue, due today, due in the next 7 days, and the nearest deadline.

---

## The sheet

One row per task, spreadsheet style.

| Column | Notes |
|---|---|
| # | Row number |
| Task | Title, plus the first line of the description under it |
| Status | Dropdown, cell is filled with the status color |
| Assigned | Pastel name tags (first 3, then +N) |
| Team | Team tag, or `--` |
| Due date / time | Date and time inputs, colored by how close the deadline is |

- Click a row to select it and open its notes box underneath.
- Double-click a row (officer) to edit every field in a modal.
- Click a column header to sort. Task, Status, Assigned and Due are sortable. Click again to reverse. Default is due date, soonest first, undated last.
- Status chips filter by status and show counts. The search box matches title, description, assignee and team. The dropdown filters by person.
- **Show Finished** swaps the sheet to archived tasks.
- **Export CSV** downloads the current view, ready to open in Excel. It includes a due state column so the colors survive the export.

---

## Due dates and times

Every task can carry a date and an optional time. Set them in the row, or use the date fields in the task modal with the Today / Tomorrow / In 1 week / Clear date buttons.

Cells are colored the way Excel conditional formatting would do it:

| State | Fill | Meaning |
|---|---|---|
| Overdue | Red `#FFC7CE` | Deadline passed, label shows `OVERDUE 3D` or `LATE 2H` |
| Due today | Amber `#FFD966` | Calendar day is today, label shows the time |
| Due soon | Light yellow `#FFF2CC` | Within 7 days |
| Later | Dark | More than 7 days out |
| No date | Black | Nothing scheduled |
| Done | Green `#C6EFCE` | Completed, no longer urgent |

Status fills: Pending `#FFEB9C`, In Progress `#BDD7EE`, In Review `#E4DFEC`, On Hold `#FCE4D6`, Done `#C6EFCE`.

Changing a status to **Done** prompts to archive the task after one second. Archived tasks leave the sheet and appear under Show Finished.

---

## Syncing

| Status | Meaning |
|---|---|
| Synced (green) | Data matches the repo |
| Unsaved changes (red) | Local edits not pushed yet |
| Syncing... (yellow) | Push in progress |
| Error | Sync failed, check connection or token |
| Offline (local copy) | Could not read the repo, running on the local copy |

Edits save to `localStorage` instantly. **Sync** pushes `data.json` to this repo through the GitHub contents API. Everyone else sees the change on their next load or refresh.

---

## Files

```
main.html                  app source, edit this
style.css                  all styles, inlined at build time
data.json                  shared data, written by the Sync button
password_template.html     StatiCrypt password screen
embed.py                   inlines CSS/JS into index.html
staticrypt + encrypt.yml   CI: build, encrypt, deploy to Pages
token.js                   created by CI only, holds API token and officer password
```

`.gitignore` excludes `token.js` (secrets) and `index.html` (build output). Never commit either.

Pushing to `main` runs `.github/workflows/encrypt.yml`, which builds `index.html`, encrypts it with StatiCrypt, and deploys to GitHub Pages. Changes to `data.json` alone do not trigger a rebuild.

Secrets required in the repo settings: `DECRYPTION_PASSPHRASE`, `SYNC_TOKEN`, `OFFICER_PASSWORD`.
