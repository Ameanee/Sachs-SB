import settings

p = settings.PREFIX

# TODO: add emojis
content = [
    f"""# Utility Commands
> `{p}user [user]` - Shows user info
> `{p}server` - Shows server info
> `{p}block [user]` - Blocks a user
> `{p}unblock [user]` - Unblocks a user
> `{p}groupchat [users]` - Creates a group chat
> `{p}status [type] [name]` - Changes your status
> `{p}spam [count] [text]` - Spams text
> `{p}aspam [count] [text]` - More advanced spam
> `{p}iplookup [ip]` - Finds ip info""",

    f"""# Fun Commands
> `{p}ask_ai [question]` - Ask AI!"""
]