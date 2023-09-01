# Daily

![image](https://github.com/marcos-venicius/daily/assets/94018427/630c6731-d667-47b0-b677-a947892ce254)


Every software engineer has a daily first thing in the morning!

How about organizing in one place and with a CLI that has only two commands?

# Table of contents

- [Installing](#installing)
- [How to use](#how-to-use)
- [Uninstalling](#uninstalling)
- [Tools](#tools)

# Installing

**Will ask sudo**

```bash
git clone https://github.com/marcos-venicius/daily.git ~/.daily && chmod u+x ~/.daily/main.py && sudo ln -s ~/.daily/main.py /bin/daily && clear && daily --help
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

# Uninstalling

**Will ask sudo**

```bash
rm -rf ~/.daily && sudo rm -rf /bin/daily
```

# Tools

- [x] Create daily
- [x] Open current daily
- [x] Show daily history
- [ ] Open daily at specific date