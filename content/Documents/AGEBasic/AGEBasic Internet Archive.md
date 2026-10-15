#agebasic #packs

# AGEBasic and the Internet Archive

You can publish your cabinets on the [Internet Archive](https://archive.org) (archive.org) so other players can download them, and an [[AGEBasic programing|AGEBasic]] program can list and download them. The players don't need an archive.org account.

You upload your cabinet `.zip` files to an archive.org **item** and share the item's **identifier** (for example `cabinet-pack-1-1`) or its address (`https://archive.org/details/cabinet-pack-1-1`).

> [!warning] Everything on archive.org is public and nearly permanent.
> Only upload what you have the right to share. **Never put ROMs inside the cabinet zips.** If archive.org takes an item down, it disappears for everyone.

## Naming rules

| What | Rule | Example |
|---|---|---|
| Item identifier | Lowercase letters, digits and `-`. Chosen once, it can't be changed. Unique in all archive.org. | `ageofjoy-curif-pack-1` |
| Cabinet file | One `.zip` per cabinet, lowercase letters, digits, `-` and `_`, no spaces. | `galaga.zip` |
| Cabinet description (optional) | A custom metadata field **named after the cabinet** (without `.zip`). The value is the description. | field `galaga` = `The standard Galaga cabinet` |

## Upload with the website

1. Log in at archive.org and click **Upload**.
2. Drag the cabinet zips.
3. Fill the form: **Page URL** (the identifier), **Title**, **Description**, subjects `ageofjoy` and `cabinet`, media type **Software**.
4. In **Add additional metadata**, add one row per cabinet: field name `galaga`, value with the description.
5. Click **Upload and Create Your Item** and wait: archive.org processes the item in the background, it can take minutes or hours.

To update the pack later use **Edit item**: add files, replace a cabinet by uploading a file with the same name, delete files or edit the descriptions. The players keep using the same identifier.

## Check your pack

Open `https://archive.org/metadata/<identifier>` in a browser. You should see every zip in `"files"` and your descriptions inside `"metadata"`. If there is a `"pending_tasks"` entry archive.org is still processing the item; `"is_dark": true` means it was taken down.

## Use a pack from AGEBasic

Functions: `IALoad`, `IAStatus`, `IAInfo`, `IACabs`, `IACabInfo`, `IADownload`, `IADownloadStatus` and `IADownloadProgress`. They are explained, with an example, in [[AGEBasic programing#Internet Archive and downloads]].

A downloaded cabinet is checked against the md5 that archive.org publishes, and it is installed the next time you start Age of Joy or load a room. Packs published on itch.io are listed in [[Cabinet packs/index|Cabinet packs]].
