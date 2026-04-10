# SoftwareManager-Server
SoftwareManager-Server is a part of the backend for [SoftwareManager](https://github.com/KeksPirates/SoftwareManager).
This is a lightweight API that serves the purpose of being able to search Rutracker without having to login yourself, simplifying usage for SoftwareManager.

## API Docs
API Docs can be found at https://softwaremanager.xyz/api

---


# Selfhosting


## How to obtain & set your Rutracker session cookie

1. Go to [rutracker.org](https://rutracker.org) and log in to your account.
2. Open your browser's Developer Tools (usually by pressing `F12` or `Ctrl+Shift+I`).
3. Navigate to the **Storage** or **Application** tab, then find **Cookies** for rutracker.org.
4. Locate the cookie named `bb_session` and copy its value.
5. Create a file named `.env` in the project root directory.
6. Add the following line to your `.env` file, replacing `{cookie}` with your copied value:

   ```
   bb_session={cookie}
   ```

7. Save the `.env` file.

Your session cookie is now set up for use with the Server.

## Server Setup Recommendations

On our VPS, we use Gunicorn to run our Flask server, with Nginx as a reverse proxy. If you want to run the server just for yourself, this isn't needed. You can simply run it directly with Flask:

```bash
python3 server.py
```

> [!NOTE]
> The server runs on Port 8080 by default.
> You can change that by modifying the "Port" variable 
> in the server.py file

