import subprocess

phone = "+14254208933"
message = "Testing from script."

script = f'''
tell application "Messages"
    set targetService to 1st service whose service type = iMessage
    set targetBuddy to buddy "{phone}" of targetService
    send "{message}" to targetBuddy
end tell
'''

subprocess.run(["osascript", "-e", script])