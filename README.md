# ELC Project Management

A password-protected project management tool for teams. Organize projects, teams, and tasks with shared data synced to GitHub.

---

## Login

Open the site and enter the team password. The page decrypts and the app loads.

The first time you visit, sample data is pre-loaded (Website Redesign, Mobile App v2, Design Team, Dev Team). The app automatically fetches the latest shared data from the repo on load.

---

## Interface

Three panels side by side:

```
|  PROJECTS  |   TEAMS    |     TASKS      |
|            |            |                |
| Project A  | Team Name  | Task 1  [Done] |
| Project B  | [Alice]    | Task 2  [Prog] |
|            | [Bob]      | Task 3  [Pend] |
|            |            |                |
| [+ Add]    | [+ Add]    | [+ Add]        |
| [Delete]   | [Edit]     | [Delete]       |
|            | [Delete]   | [Show Fini'd]  |
```

---

## Projects

### Create a project
Click **+ Add** at the bottom of the Projects panel. Type a name.

### Select a project
Click any project in the list. The Teams and Tasks panels update to show only what belongs to that project.

### Delete a project
Select a project, then click **Delete**. This removes the project and all its teams and tasks.

---

## Teams

Teams are groups of people that belong to a project. Select a project first to see its teams.

### Create a team
Click **+ Add** in the Teams panel. A modal opens:
- **Team Name** — name for the team (e.g., "Design Team")
- **Members** — comma-separated list of names (e.g., "Alice, Bob, Charlie")

Click OK. The team appears in the middle panel with each member shown as a colored tag.

### Select a team
Click any team. The team name is highlighted with an orange border.

### Edit a team
Select a team, then click **Edit**. The modal opens pre-filled with the current name and members. Change and save.

### Delete a team
Select a team, then click **Delete**. The team is removed from the project and any tasks assigned to it lose that reference.

---

## Tasks

### Create a task
Select a project, then click **+ Add** in the Tasks panel. A modal opens:

- **Title** — what the task is
- **Description** — details about the task (optional)
- **Assign Team** — dropdown of teams assigned to this project (optional)
- **Assign People** — comma-separated list of names (optional, can be anyone even if not on a team)

Click OK. The task appears in the task list with colored tags showing who it's assigned to.

### Select a task
Click a task in the list. Its description textarea appears below it (if it has one). Click again to deselect.

### Change status
Each task has a colored dropdown showing its status. Click to change:

| Status | Color | Meaning |
|---|---|---|
| Pending | Gold | Not started |
| In Progress | Blue | Currently being worked on |
| In Review | Purple | Awaiting review |
| Done | Green | Completed |
| On Hold | Orange | Paused or blocked |

Changing to **Done** triggers a 1-second delay, then asks: "Archive this task?" If you confirm, the task is archived and hidden from the main view.

### Edit description
Select a task to reveal its description textarea. Type or edit, then click away to save.

### Delete a task
Select a task, then click **Delete**. Confirms first, then removes it permanently.

### View finished tasks
Click **Show Finished** in the Tasks panel footer. This switches the view to show only archived tasks. The button changes to **Show Current** — click it to go back.

---

## Syncing

The **Sync** button and status are in the top-right corner.

| Status | Meaning |
|---|---|
| Synced (green) | Data is up to date with the repo |
| Unsaved (red) | You've made changes that haven't been pushed |
| Syncing... (yellow) | Currently pushing to the repo |
| Error (red) | Sync failed — check your connection |
| Offline | Couldn't fetch latest data (runs from local copy) |

**Click Sync** to push your changes to the shared repo. Other team members will see your changes when they load or refresh the page.

The app auto-saves to your browser's localStorage instantly. The Sync button is only needed to share changes with the team.

---

## Tips

- Multiple people can work at the same time. After someone else syncs, refresh the page (or wait for auto-load) to get their changes.
- Tasks can be assigned to multiple people even if they're on different teams — just type all their names in the "Assign People" field.
- Team members are just names. There are no user accounts — the password gates the whole app.
