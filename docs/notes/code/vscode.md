# Vscode

## Snippets

Use [snippets](https://code.visualstudio.com/docs/editor/userdefinedsnippets) to define macros on vscode (search for configure snippets)

```json title="markdown.json"
	"Generate code block":{
		"prefix":"cb",
		"body":[
			"```${1:langage} title=\"${2:}\"",
			"${3:code}",
			"```",
			""
		],
		"description":"generate code block"
	},
	"Generate flashcard": {
		"prefix": "fc",
		"body": [
			"??? question \"${1:Question Text}\"",
			"    ${2:$CLIPBOARD}",
			"    ##### id: $RANDOM_HEX, box: 1, score: 0/0, next: $CURRENT_DATE/$CURRENT_MONTH/$CURRENT_YEAR, last: $CURRENT_DATE/$CURRENT_MONTH/$CURRENT_YEAR",
			""
		],
		"description": "generate flashcard"
	}
```

## Flashcards