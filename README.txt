TRIVIA PWA TERMINAL — MOBILE, OFFLINE, NO SERVER

WHAT THIS DOES
- Converts your current trivia.db into a tiny mobile web app.
- Same terminal-style game.
- Quick Play / Learn New / Review Due / Association Drill / Statistics.
- Once installed on iPhone, works offline and your Mac may be OFF.
- Progress is stored on the iPhone.
- Export Progress button gives you a JSON backup.

BUILD FROM YOUR CURRENT DB
1) Put this folder in Downloads.
2) Terminal:
   cd ~/Downloads/trivia_pwa_terminal
   python3 build_mobile_app.py

3) The ready app will be:
   ~/Downloads/trivia_pwa_terminal/dist/

HOST IT ONCE
Upload the CONTENTS of dist/ to any static HTTPS host.
No Python server, VPS, or database server is required.

IPHONE
1) Open the HTTPS address in Safari.
2) Share -> Add to Home Screen.
3) Open Trivia from the icon.
4) After the first successful load it works offline.

IMPORTANT
This first simple version stores new progress on the iPhone itself.
It starts with the progress/statistics exported from your Mac at build time.
