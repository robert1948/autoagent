# 🚀 AutoAgent Codespaces Setup Checklist

This checklist outlines our team’s choices for setting up GitHub Codespaces for the AutoAgent project. Use this to ensure consistency across our development environment.

---

## ✅ 1. Dotfiles

- **Choice:** Disabled (default)
- **Reason:** We do not have custom dotfiles to auto-install. If needed, set up dotfiles first.

---

## ✅ 2. Secrets

- **Choice:** Add only environment variables needed for Codespaces (like `DJANGO_SECRET_KEY`, `DATABASE_URL`, etc.).
- **Action:**
  - Click **New secret** in Codespaces settings.
  - Name it clearly (e.g., `AUTOAGENT_API_KEY`).
  - Keep secrets minimal and secure.

---

## ✅ 3. GPG Verification

- **Choice:** Disabled (optional)
- **Reason:** Only enable if we want to sign commits with GPG keys for extra security.

---

## ✅ 4. Settings Sync

- **Choice:** ✅ Enabled
- **Reason:** Ensures everyone’s Codespaces uses their preferred VS Code theme, keybindings, and extensions.

---

## ✅ 5. Notifications

- **Choice:** ✅ Enabled
- **Reason:** Receive email alerts before Codespaces are deleted (protects work).

---

## ✅ 6. Trusted Repositories

- **Choice:** All repositories
- **Reason:** Easier to work across different repos and branches without re-approving every time.

---

## ✅ 7. Access and Security

- **Choice:** ✅ Disabled (default)
- **Reason:** Codespaces are limited to the repo they were created for. No extra access needed.

---

## ✅ 8. Editor Preference

- **Choice:** ✅ Visual Studio Code
- **Reason:** Team members can connect Codespaces to their local VS Code for a better editing experience.
- **Optional:** Visual Studio Code for the Web is available if needed (browser-only).

---

## 📌 Summary Table

| Setting              | Choice                      | Rationale/Comments                   |
| -------------------- | --------------------------- | ------------------------------------ |
| Dotfiles             | Disabled                    | No team dotfiles yet                 |
| Secrets              | Add only what’s needed      | Keep minimal and secure              |
| GPG Verification     | Optional (disabled for now) | Signing not required for this repo   |
| Settings Sync        | ✅ Enabled                  | Personalized VS Code environment     |
| Notifications        | ✅ Enabled                  | Inactivity alerts to avoid data loss |
| Trusted Repositories | All repositories            | Seamless cross-repo work             |
| Access & Security    | ✅ Disabled                 | Only repo-specific access needed     |
| Editor Preference    | ✅ Visual Studio Code       | Best editing experience              |

---

### 📁 Share with Team

- Save this file as `codespaces-setup.md` in the project’s root.
- Discuss in onboarding or dev syncs.
- Adjust if team preferences evolve.

---

🎉 Let’s keep our Codespaces efficient and consistent! 🚀
