<h1>Renamer</h1>
<h2>Simple shell tool for file renaming written in python</h2>
<h3>Install</h3>
<p>
You will need pip tool for python to install renamer into your shell environment.<br />
If you have python 3.4+ you don't have to install pip.<br />
If you are running lower version you can find instructions on how to install pip here: <a href="http://www.pip-installer.org/en/latest/installing.html">http://www.pip-installer.org/en/latest/installing.html</a><br />
<br />
After you install pip:<br />
<br />
$ git clone https://github.com/capJavert/renamer.git<br />
$ cd renamer<br />
$ pip install --editable .<br />
</p>
<h3>Usage</h3>
<p>
Usage: renamer [OPTIONS]<br />
<br />
Options:<br />
  --path TEXT    - Path to directory where files/directories you want renamed<br />
                 are located. Defaults to current directory if not set.<br />
  --change TEXT  - Part of the file/directory name you want to replace.<br />
  --to TEXT      - String you want to replace --change string to.<br />
  --help         - Show help.<br />
</p>