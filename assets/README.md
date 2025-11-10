# Assets Folder

## Logo

Please place the SolarKH logo image here as `logo.png`

The logo will be displayed in:
- Welcome message (`/start`)
- Language switch confirmation
- Product catalog (`/products`)
- Education center (`/learn`)

**Logo Requirements:**
- Format: PNG (recommended) or JPG
- Size: 500x500px or similar square ratio
- File name: `logo.png`

**Current logo features:**
- Blue "SOLAR" text
- Orange "KH" text
- House with solar panels
- Sun icon

Once the logo is added here, update the `LOGO_URL` in `config.py` to point to the correct location.

For GitHub hosting:
```python
LOGO_URL = "https://raw.githubusercontent.com/chhany007/solarkh_bot_new/main/assets/logo.png"
```

For local file:
```python
LOGO_URL = "file:///path/to/assets/logo.png"
```

Or use a direct URL from your hosting service.
