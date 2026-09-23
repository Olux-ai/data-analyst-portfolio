# Portfolio Website: Deployment and Photo Guide

This folder contains your finished website. It deploys for free with **GitHub Pages**, using the repository you already have (`data-analyst-portfolio`).

Your live address will be:

```text
https://olux-ai.github.io/data-analyst-portfolio/
```

---

## What is in this folder

```text
portfolio-site/
├── DEPLOYMENT_GUIDE.md          (this guide)
└── docs/                        (the website; this is the folder you upload)
    ├── index.html               (the page)
    ├── images/
    │   ├── profile.jpg          (your portrait)
    │   ├── pizza-home.jpg       (Pizza Sales dashboard, Home page)
    │   └── pizza-best.jpg       (Pizza Sales dashboard, Best/Worst Sellers page)
    └── assets/
        └── Adebayo_Olumide_Philip_Data_Analyst_Resume.pdf   (the Download resume button)
```

---

## Part 1: Deploy the website

### Step 1: Unzip

Unzip `portfolio-site.zip` on your computer. You should see the `docs` folder.

### Step 2: Upload the `docs` folder to your repository

1. Go to `https://github.com/Olux-ai/data-analyst-portfolio`.
2. Click **Add file**, then **Upload files**.
3. Drag the whole **`docs`** folder into the box. Use Chrome or Edge, because they keep the folder structure when you drag a folder in.
4. Wait until every file is listed, including the ones inside `images` and `assets`.
5. In **Commit changes**, type `Add portfolio website` and click **Commit changes**.

Check: open the repository. You should now see a `docs` folder next to `Excel`, `SQL` and `PowerBI`.

### Step 3: Turn on GitHub Pages

1. In the repository, click **Settings**.
2. In the left menu, click **Pages**.
3. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
4. Under **Branch**, choose **main** and, in the folder box beside it, choose **/docs**. Click **Save**.

### Step 4: Open your website

Wait one to three minutes, then refresh the Pages settings screen. A message appears at the top: **Your site is live at ...**. Click the link.

If it says 404, wait another minute and refresh. You can watch progress in the **Actions** tab: look for **pages build and deployment**.

> The repository must be **public** for free GitHub Pages.

### Step 5: Test it

- Your photo shows in the top-left corner and in the **About me** section.
- Both Pizza Sales dashboard tabs show their images.
- **Download resume** downloads your PDF.
- Click all four project links (Excel workbook, SQL queries, Power BI project, and the Python GitHub link) and confirm each opens.

---

## Part 2: Add or change your pictures

All pictures live in `docs/images/`. The page looks for **exact file names**, so keep the names as shown (lowercase, `.jpg`).

| File name | What it shows | Best size |
|---|---|---|
| `profile.jpg` | Your portrait (top-left corner and About me) | Square, at least 800 x 800 pixels, under 300 KB |
| `pizza-home.jpg` | Pizza Sales dashboard, Home page | About 1200 pixels wide |
| `pizza-best.jpg` | Pizza Sales dashboard, Best/Worst Sellers | About 1200 pixels wide |
| `superstore-dashboard.jpg` | Your Excel dashboard for Superstore. **Optional**: it appears above the Superstore charts as soon as you add it, and stays hidden until then | About 1200 to 1600 pixels wide |

### To replace a picture

1. On GitHub, open the repository and go to `docs/images`.
2. Click **Add file**, then **Upload files**.
3. Drag in the new picture **with exactly the same file name** as the one you are replacing.
4. Click **Commit changes**. The new file replaces the old one.
5. Wait a minute, then press **Ctrl + Shift + R** (Windows) or **Cmd + Shift + R** (Mac) on your website to see the change.

### To add the Superstore dashboard picture

1. Take a screenshot of your Excel dashboard.
2. Save it as `superstore-dashboard.jpg` (if it is a `.png`, open it in Paint or Photos and save it again as JPG).
3. Upload it to `docs/images` as above.

### Picture tips

- **Profile photo:** use a clear, well-lit photo where your face fills about half the frame. If your new photo is not square, crop it to a square first.
- **Screenshots:** crop out anything that is not the dashboard, and keep each file under about 300 KB so the page loads fast.
- **Names matter:** GitHub treats `Profile.jpg` and `profile.jpg` as different files. If a picture does not appear, the file name is the first thing to check.

Want more pictures on the page (for example a gallery)? Ask me and I will add a section for them.

---

## Part 3: After it is live

1. **Add the link to LinkedIn:** Profile, then **Contact info**, then **Website**. Also add it to the **Featured** section.
2. **Add the link to GitHub:** on the repository page, click the gear icon beside **About** and paste the address into **Website**.
3. **Put it on your resume:** add the website next to your LinkedIn and GitHub links.
4. **Link previews:** the page already has a preview title, description and your photo for when you share the link. These lines in `docs/index.html` (`og:image` and `og:url`) assume the address shown at the top of this guide. If your address is different, edit those two lines.

---

## Updating the website later

- **Small text changes:** open `docs/index.html` on GitHub, click the pencil icon, edit, and commit. The site updates in about a minute.
- **New resume:** upload the new PDF to `docs/assets` with the same file name.
- **Bigger changes:** send me what you want changed and I will give you a new `index.html` to upload.

---

## Optional: your own web address

A custom domain (for example `adebayoolumide.com`) makes the site look more professional. Buy the domain from any registrar, then in **Settings, Pages, Custom domain** enter it and follow GitHub's DNS instructions. Do this after the site is live.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| The page shows 404 | Wait a few minutes. Check Settings, Pages shows **main** and **/docs**. Check `index.html` is inside `docs`, not inside a second folder. |
| The page shows but has no pictures | The `images` folder was not uploaded, or file names differ in spelling or capital letters. |
| The old picture still shows | Hard refresh with Ctrl + Shift + R (Cmd + Shift + R on Mac). |
| Download resume does nothing | Check `docs/assets` contains the PDF with the exact name `Adebayo_Olumide_Philip_Data_Analyst_Resume.pdf`. |
| A project link opens a "404" page on GitHub | The file or folder path on GitHub is different from the link. Open the file on GitHub, copy its address, and send it to me to update the link. |
| The `docs` folder did not upload with its contents | Upload in Chrome or Edge, or upload `index.html` first and then create the `images` and `assets` folders with **Add file, Create new file** (type `images/` in the name box) and upload the pictures into them. |

---

## Using Git instead (optional)

If you use Git on your computer, copy the `docs` folder into your local `data-analyst-portfolio` folder, then run:

```bash
git add docs
git commit -m "Add portfolio website"
git push
```

Then continue from Step 3.
