# Daily

![image](https://github.com/marcos-venicius/daily/assets/94018427/630c6731-d667-47b0-b677-a947892ce254)


Every software engineer has a daily first thing in the morning!

How about organizing in one place and with a CLI that has only two commands?

# Table of contents

- [Installing](#installing)
- [Updating](#updating)
- [Uninstalling](#uninstalling)
- [How to use](#how-to-use)
- [Tools](#tools)

# Installing

**Will ask for sudo**

Tools that you will need

- Git
- Python

**This installation should work on many Unix systems, but i just tested on ubuntu**

```bash
git clone https://github.com/marcos-venicius/daily.git ~/.daily && chmod u+x ~/.daily/main.py && sudo ln -s ~/.daily/main.py /bin/daily && clear && daily --help
```

# Updating

this command will update your daily tool

```bash
daily --update
```

# Uninstalling

**Will ask for sudo**

```bash
rm -rf ~/.daily && sudo rm -rf /bin/daily
```

# How to use?

To create a new daily, or access the daily just type this on your terminal:

```bash
daily
```

If you've run the command before, and taken notes, the daily file will be opened in VIM, if you haven't run it before, it will create a template for you

**Please, don't remove the default template structure, it is used to get the correct history**

Keys like: `Summary`, `Notes`, `In the morning`, `In the afternoon` and the header, are special "keys", **please, don't delete them**

To see your daily history:

```bash
daily --history
```

this command will show your daily history with a short summary presentation

# Tools

- [x] Create daily
- [x] Open current daily
- [x] Show daily history
- [x] Create command to update the CLI
- [ ] Today daily on `VIEW MODE`
- [ ] Open daily at specific date