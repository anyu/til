
### Retrieve source code for a chrome extension

#### No installation required

1. Download the CRX file:

```sh
curl -L "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=[PRODVERSION]&acceptformat=crx2,crx3&x=id%3D[EXTENSIONID]%26uc" -O
```
- `[PRODVERSION]` = Chrome version, minimum 31.0.1609.0
- `[EXTENSIONID]` = ID of the extension

eg.

```
curl -L "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=129.0.0.0&acceptformat=crx2,crx3&x=id%3Depcnnfbjfcgphgdmggkamkmgojdagdnn%26uc" -O
```

2. Zip the file: `mv crx crx.zip`
3. Unzip it: `unzip crx.zip`

#### If installed
1. Find path to directory for chrome profile via: `chrome://version` > `Profile Path`
	- eg. `$HOME/Library/Application Support/Google/Chrome/Default`
2. Match chrome extension ID with directory
