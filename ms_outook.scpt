set my_recipient_name to "fName lName"
set my_recipient to "eMail@DOMAIN.com"
set my_subject to "Hello from automation!"
set my_content to "Message Body"
set my_app to "Microsoft Outlook"
set my_xfile to "File_Path"
tell application "Microsoft Outlook"
	activate
	set my_message to make new outgoing message with properties {subject:my_subject, content:my_subject}
	make new recipient at my_message with properties {email address:{address:my_recipient}}
	tell my_message
		make new attachment with properties {file:my_xfile}
	end tell
	send my_message
end tell
