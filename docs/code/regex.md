# Regex

Use [regex101](https://regex101.com/) to test regular expressions

## Python
```python title=""
import re
```

### Functions
| Function    | Description                                                       | example |
| ----------- | ----------------------------------------------------------------- | ------- |
| re.findall  | Returns a list containing all matches                             |         |
| re.finditer | Return an iterable of match objects (one for each match)          |         |
| re.search   | Returns a Match object if there is a match anywhere in the string |         |
| re.findall  | Returns a list containing all matches                             |         |
| re.split    | Returns a list where the string has been split at each match      |         |
| re.sub      | Replaces one or many matches with a string                        |         |
| re.compile  | Compile a regular expression pattern for later use                |         |
| re.escape   | Return string with all non-alphanumerics backslashed              |         |


### Examples
```python title="re.findall"
>>> re.findall(r'\bs?pare?\b', 'par spar apparent spare part pare')
['par', 'spar', 'spare', 'pare']
>>> re.findall(r'\b0*[1-9]\d{2,}\b', '0501 035 154 12 26 98234')
['0501', '154', '98234']
```

```python title="re.finditer"
>>> m_iter = re.finditer(r'[0-9]+', '45 349 651 593 4 204')
>>> [m[0] for m in m_iter if int(m[0]) < 350]
['45', '349', '4', '204']
```

```python title="re.split"
>>> re.split(r'\d+', 'Sample123string42with777numbers')
['Sample', 'string', 'with', 'numbers']
```

```python title="re.sub"
>>> ip_lines = "catapults\nconcatenate\ncat"
>>> print(re.sub(r'^', r'* ', ip_lines, flags=re.M))
* catapults
* concatenate
* cat
```

```python title="re.compile"
>>> pet = re.compile(r'dog')
>>> type(pet)
<class '_sre.SRE_Pattern'>
>>> bool(pet.search('They bought a dog'))
True
>>> bool(pet.search('A cat crossed their path'))
False
```


```python title="re.search"
>>> sentence = 'This is a sample string'
>>> bool(re.search(r'this', sentence, flags=re.I))
True
>>> bool(re.search(r'xyz', sentence))
False
```

## Example
!!! example "email address `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`"
    - starts with one or more alphanumeric characters, periods, underscores, percents, pluses, or hyphens
    - expects the `@` symbol, followed by the domain name, which can have alphanumeric characters and hyphens
    - looks for a period and a domain suffix (like `com` or `net`)

!!! example "url `https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/[\w&%?#-]+)*`"
    - starts with the `http` or `https` protocol, followed by `://`
    - matches the domain name and optional path components, which can contain alphanumeric characters, underscores, percents, question marks, hashes, and hyphens

!!! example "date in YYYY-MM-DD format `(\d{4})-(\d{2})-(\d{2})`"
    - captures four digits for the year, two digits for the month, and two digits for the day, separated by hyphens
    - each of these components is captured in its own capture group

!!! example "filename with specific extension `(?i)^(?!backup_).*\.(?:jpg|jpeg|png)$`"
    This pattern matches filenames that are not prefixed with `backup_` (case insensitive due to `(?i)`) and ends with the extensions `.jpg`, `.jpeg`, or `.png`

    - the `(?!...)` part is a negative lookahead that ensures the filename doesn't start with `backup_`
    - the `(?:...)` part is a non-capturing group for the file extensions

!!! example "number not preceded by `$` or `£` `(?<![£$])\b\d+\b`"
    This pattern matches numbers that are not immediately preceded by either a `$` or a `£` symbol

    - `(?<!...)` part is a negative lookbehind. It ensures that the matched number does not have the specified prefix
    - `\b` parts are word boundaries, ensuring that we match whole numbers

!!! example "match HTML tags but not self-closing ones `<(?!\w+/>)[a-zA-Z]*>(?!<).*?</\w+>`"
    This pattern matches HTML opening and closing tags and their content, but skips self-closing tags like <img/>

    - the `(?!\w+/>)` part is a negative lookahead ensuring we don't match self-closing tags
    - the `(?!<)` is another negative lookahead ensuring we don't match another opening tag immediately after the first one, which would make it invalid HTML
    - the non-capturing group `(?:...)` ensures that we don't create unnecessary capturing groups for the matched content

## Cheatsheet

### Anchors
| Pattern | Description                                             | Example                                                                 |
| ------- | ------------------------------------------------------- | ----------------------------------------------------------------------- |
| `^`     | Start of string, or start of line in multi-line pattern | `^Hello` matches the string "Hello" only if it's at the start           |
| `\A`    | Start of string                                         | `\AHello` matches the string "Hello" only if it's at the very beginning |
| `$`     | End of string, or end of line in multi-line pattern     | `world$` matches the string "world" only if it's at the end             |
| `\Z`    | End of string                                           | `world\Z` matches the string "world" only if it's at the very end       |
| `\b`    | Word boundary                                           | `\bword\b` matches the string "word" only if it's a whole word          |
| `\B`    | Not word boundary                                       | `\Bord\B` matches the "ord" in "ordinary" but not in "order".           |
| `\<`    | Start of word                                           | `\<word` matches "word" in "wording" but not in "sawword".              |
| `\>`    | End of word                                             | `word\>` matches "word" in "saw word" but not in "wording".             |

### Groups and Ranges
| Pattern | Description                        | Example                                     |
| ------- | ---------------------------------- | ------------------------------------------- |
| .       | Any character except new line (\n) | a.b matches "a.b", "axb", "a1b", etc        |
| (a\|b)  | a or b                             | (cat\|dog) matches "cat" or "dog"           |
| (...)   | Group                              | (ab)+ matches "ab", "abab", "ababab", etc   |
| (?:...) | Passive (non-capturing) group      | (?:ab)+ matches "ab", "abab", "ababab", etc |
| [abc]   | Range (a or b or c)                | [aeiou] matches any vowel                   |
| [^abc]  | Not (a or b or c)                  | [^aeiou] matches any consonant              |
| [a-q]   | Lower case letter from a to q      | [a-z] matches any lowercase letter          |
| [A-Q]   | Upper case letter from A to Q      | [A-Z] matches any uppercase letter          |
| [0-7]   | Digit from 0 to 7                  | [0-9] matches any digit                     |
| \x      | Group/subpattern number "x"        | (\d)\1 matches "11", "22", "33", etc        |


!!! note "Ranges are inclusive"

### Assertions
| Pattern | Description              | Example                                                      |
| ------- | ------------------------ | ------------------------------------------------------------ |
| ?=      | Lookahead assertion      | x(?=y) matches "x" only if it's followed by "y".             |
| ?!      | Negative lookahead       | x(?!y) matches "x" only if it's not followed by "y".         |
| ?<=     | Lookbehind assertion     | (?<=y)x matches "x" only if it's preceded by "y".            |
| ?<!     | Negative lookbehind      | (?<!y)x matches "x" only if it's not preceded by "y".        |
| ?>      | Once-only Subexpression  | a(?>b\|bc)c matches "abc", but not "abcc".                   |
| ?()     | Condition [if then]      | (?(?=y)xy\|x) matches "xy" or "x" based on the condition     |
| ?()\|   | Condition [if then else] | (?(?=y)xy\|xz) matches "xy" if "y" follows or "xz" otherwise |
| ?#      | Comment                  | a(?#This is a comment)b matches "ab".                        |

### Quantifiers
| Pattern | Description | Example                                   |
| ------- | ----------- | ----------------------------------------- |
| ?       | 0 or 1      | ab?c matches "ac" or "abc".               |
| *       | 0 or more   | ab*c matches "ac", "abc", "abbc", etc     |
| +       | 1 or more   | ab+c matches "abc", "abbc", etc           |
| {3}     | Exactly 3   | a{3} matches "aaa".                       |
| {3,}    | 3 or more   | a{3,} matches "aaa", "aaaa", "aaaaa", etc |
| {3,5}   | 3, 4 or 5   | a{3,5} matches "aaa", "aaaa", "aaaaa".    |

!!! note "?"
    Add a `?` to a quantifier to make it ungreedy.

    For example, `a+?` matches the shortest sequence of "a"s.

### Common Metacharacters
| Pattern | Description                      | Example                                                                                |
| ------- | -------------------------------- | -------------------------------------------------------------------------------------- |
| ^       | Start of string                  | ^Hello matches "Hello" at the start of a string                                        |
| [       | Beginning of a character class   | [aeiou] matches any vowel                                                              |
| .       | Any character except new line    | . matches any character except for a new line character                                |
| $       | End of string                    | world$ matches "world" at the end of a string                                          |
| {       | Start of a quantifier            | a{3} matches "aaa"                                                                     |
| *       | 0 or more of the preceding token | ab*c matches "ac", "abc", "abbc", etc                                                  |
| (       | Start of a capturing group       | (abc) captures "abc" as a group                                                        |
| \       | Escape character                 | \$ matches a literal dollar sign ($)                                                   |
| +       | 1 or more of the preceding token | ab+c matches "abc", "abbc", etc                                                        |
| )       | End of a capturing group         | (abc) captures "abc" as a group                                                        |
| l       | Alternation (OR)                 | a                                                       \| b matches either "a" or "b" |
| \|      | 0 or 1 of the preceding token    | ab?c matches "ac" or "abc"                                                             |
| <       | Less than                        | a < b matches "a < b"                                                                  |
| >       | Greater than                     | a > b matches "a > b"                                                                  |

!!! note "The escape character is usually `\`"

### Escape Sequences
| Pattern | Description                | Example                                   |
| ------- | -------------------------- | ----------------------------------------- |
| \       | Escape following character | \\ matches the backslash character itself |
| \Q      | Begin literal sequence     | \Q.*\E matches the literal string ".*".   |
| \E      | End literal sequence       |                                           |

!!! note "**Escaping**"
    **Escaping** is a way of treating characters which have a special meaning in regular expressions literally, rather than as special characters.

### Special Characters
| Pattern | Description         | Example                                                                            |
| ------- | ------------------- | ---------------------------------------------------------------------------------- |
| \n      | New line            | Hello\nWorld matches "Hello" followed by a new line and then "World"               |
| \r      | Carriage return     | Hello\rWorld matches "Hello" followed by a carriage return and then "World"        |
| \t      | Tab                 | Hello\tWorld matches "Hello" followed by a tab character and then "World"          |
| \v      | Vertical tab        | Hello\vWorld matches "Hello" followed by a vertical tab character and then "World" |
| \f      | Form feed           | Hello\fWorld matches "Hello" followed by a form feed character and then "World"    |
| \xxx    | Octal character xxx | \141 matches the letter "a"                                                        |
| \xhh    | Hex character hh    | \x41 matches the letter "A"                                                        |

### Character Classes
| Pattern | Description                         | Example                                    |
| ------- | ----------------------------------- | ------------------------------------------ |
| \c      | Control character                   | \cM matches the control character "Return" |
| \s      | White space                         | a\s+b matches "a b", "a b"                 |
| \S      | Not white space                     | \Sa\S matches "aB", "1_"                   |
| \d      | Digit                               | \d\d matches "12", "34"                    |
| \D      | Not digit                           | \D\D matches "AB", "a_"                    |
| \w      | Word (alphanumeric plus underscore) | \w\w\w matches "abc", "123", "a_1"         |
| \W      | Not word                            | A\WZ matches "A!Z", "A@Z"                  |

### POSIX
| Pattern    | Description                           | Example                                                      |
| ---------- | ------------------------------------- | ------------------------------------------------------------ |
| [:upper:]  | Upper case letters                    | [:upper:] matches any uppercase letter like "A", "B"         |
| [:lower:]  | Lower case letters                    | [:lower:] matches any lowercase letter like "a", "b"         |
| [:alpha:]  | All letters                           | [:alpha:] matches any letter like "a", "A"                   |
| [:alnum:]  | Digits and letters                    | [:alnum:] matches any letter or digit like "a", "A", "1"     |
| [:digit:]  | Digits                                | [:digit:] matches any digit like "1", "2"                    |
| [:xdigit:] | Hexadecimal digits                    | [:xdigit:] matches any hex digit like "a", "A", "1"          |
| [:punct:]  | Punctuation                           | [:punct:] matches punctuation like "!", "@"                  |
| [:blank:]  | Space and tab                         | [:blank:] matches a space or a tab                           |
| [:space:]  | Blank characters                      | [:space:] matches any whitespace character                   |
| [:cntrl:]  | Control characters                    | [:cntrl:] matches control characters like "Return", "Escape" |
| [:graph:]  | Printed characters (excluding spaces) | [:graph:] matches characters like "a", "1", "!"              |
| [:print:]  | Printed characters and spaces         | [:print:] matches characters like "a", " ", "1", "!"         |
| [:word:]   | Digits, letters, and underscore       | [:word:] matches "a", "A", "1", "_"                          |

### Pattern Modifiers
| Pattern | Description                              | Example                                                                  |
| ------- | ---------------------------------------- | ------------------------------------------------------------------------ |
| g       | Global match                             | g flag in regular expression to match all occurrences in a string        |
| i*      | Case-insensitive                         | i flag in regular expression to perform case-insensitive matching        |
| m*      | Multiple lines                           | m flag in regular expression to match across multiple lines              |
| s*      | Treat string as single line              | s flag in regular expression to treat the string as a single line        |
| x*      | Allow comments and whitespace in pattern | x flag in regular expression to allow comments and whitespace in pattern |
| e*      | Evaluate replacement                     | e flag in regular expression to evaluate the replacement as code         |
| U*      | Ungreedy pattern                         | U flag in regular expression to make the pattern ungreedy                |

### String Replacement
| Pattern | Description             | Example                                                                                  |
| ------- | ----------------------- | ---------------------------------------------------------------------------------------- |
| $n      | nth non-passive group   | If (abc) is the first group in a regex, then $1 would replace it in a replacement string |
| $2      | "xyz" in ^(abc(xyz))$   | The second group in the regex ^(abc(xyz))$ is "xyz"                                      |
| $1      | "xyz" in ^(?:abc)(xyz)$ | The first group in the regex ^(?:abc)(xyz)$ is "xyz"                                     |
| $\`\`   | Before matched string   | $\`\` represents the portion of the string before the matched string                     |
| $'      | After matched string    | $' represents the portion of the string after the matched string                         |
| $+      | Last matched string     | $+ represents the last matched string                                                    |
| $&      | Entire matched string   | $& represents the entire matched string                                                  |


??? question "Regex: match an email adress"
    `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`

??? question "Regex: match filenames that are not prefixed with `backup_` and ends with the extensions `.jpg`, `.jpeg`, or `.png`"
    `(?i)^(?!backup_).*\.(?:jpg|jpeg|png)$`
