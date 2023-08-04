# regex

The aim is to prepare notes of regex. I am following https://docs.python.org/3/howto/regex.html#regex-howto

## Simple Patterns

Here’s a complete list of the metacharacters:

```
. ^ $ * + ? { } [ ] \ | ( )
```

`[]`: used for specifying a character class (set of characters that you wish to match). Characters can be listed individually, or as a range indicated by '-'. Examples:

- `[abc]` will match `'a'`, `'b'`, or `'c'`; same as `[a-c]`.
- `[akm$]` will match `'a'`, `'k'`, `'m'`, or `'$'`; `'$'` is a metacharacter, but not inside `[]`.

`^`: Complementing the set; as the first character. Example:

- `[^5]` will match any character except `'5'`. However, `[5^]` will match either a `'5'` or a `'^'`.

<!-- &emsp;&emsp;&emsp;&emsp; dsd -->

List of special sequence:\
`\d`
&emsp;Matches any decimal digit; this is equivalent to the class `[0-9]`.

`\D`
&emsp;Matches any non-digit character; this is equivalent to the class `[^0-9]`.

`\s`
&emsp;Matches any whitespace character; this is equivalent to the class `[ \t\n\r\f\v]`.

`\S`
&emsp;Matches any non-whitespace character; this is equivalent to the class `[^ \t\n\r\f\v]`.

`\w`
&emsp;Matches any alphanumeric character; this is equivalent to the class `[a-zA-Z0-9_]`.

`\W`
&emsp;Matches any non-alphanumeric character; this is equivalent to the class `[^a-za-z0-9_]`.

These can be included inside a character class. For example, `[\s,.]` is a character class that will match any whitespace character, or `','` or `'.'`.

## Repeating Things

`*`: previous character can be matched zero or more times. It is greedy; matching engine will try to repeat it as many times and reduce the number of tries. Example:

- `ca\*t` will match `ct` (0 `a` characters), `cat` (1 `a`), `caaat` (3 `a` characters), and so forth.

`+`: matches one or more times. Example:

- `ca+t` will match `'cat'` (1 `'a'`), `'caaat'` (3 `'a'`s), but won’t match `'ct'`.

`?`: matches either once or zero times; can be use to mark something as being optional. Example:

- `home-?brew` matches either `'homebrew'` or `'home-brew'`.

`{m,n}`: there must be at least `m` repetitions, and at most `n`; `m` and `n` are integers. Example

- `a/{1,3}b` will match `'a/b'`, `'a//b'`, and `'a///b'` but not `'ab'` or `'a////b'`.
- `{,n}` = `{0,n}`; `{m,}` = `{m,infinity}`.
- Note: `{0,}` = `*`;&emsp;`{1,}` = `+`;&emsp;`{0,1}` = `?`.

`*?`, `+?`, `??`: The `'*'`, `'+'`, and `'?'` quantifiers are all greedy. Adding `?` after the quantifier makes it perform the match in non-greedy or minimal fashion; as few characters as possible will be matched.

`*+`, `++`, `?+`
Like the `'*'`, `'+'`, and `'?'` quantifiers, those where `'+'` is appended also match as many times as possible. However, unlike the true greedy quantifiers, these do not allow back-tracking when the expression following it fails to match. These are known as _possessive quantifiers_. For example, `a*a` will match `'aaaa'` because the `a*` will match all 4 `'a'`s, but, when the final `'a'` is encountered, the expression is backtracked so that in the end the `a*` ends up matching 3 `'a'`s total, and the fourth `'a'` is matched by the final `'a'`. However, when `a*+a` is used to match `'aaaa'`, the `a*+` will match all 4 `'a'`, but when the final `'a'` fails to find any more characters to match, the expression cannot be backtracked and will thus fail to match.

## Compiling Regular Expressions

Regular expressions are compiled into pattern objects, which have methods for various operations such as searching for pattern matches or performing string substitutions.

```python
import re
p = re.compile('ab*')
p
re.compile('ab*')
```

`re.compile()` also accepts an optional _flags_ argument.

```python
p = re.compile('ab*', re.IGNORECASE)
```

## The Backslash Plague

Use Python’s raw string notation for regular expressions; so `r"\n"` is `'\'` and `'n'`, while `"\n"` is newline.

- NOTE: In following code, we see `\\` because it is created by `__repr__()` method. Python represents backslashes in strings as `\\` because the backslash is an escape character.

```python
>>> string = "\string"
>>> string
\\string

>>> print(string)
\string

>>> print(repr(string))
\\string
```

## Performing Matches

The most common style:

```python
p = re.compile( ... )
m = p.match( 'string goes here' )
if m:
    print('Match found: ', m.group())
else:
    print('No match')

# the following is also possible (more convenient)
>>> re.match(r'From\s+', 'From amk Thu May 14 19:12:10 1998')
<re.Match object; span=(0, 5), match='From '>
```

## Compilation Flags

| Flag                        | Description                                                                                                       |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| ASCII, A                    | Makes several escapes like `\w`, `\b`, `\s` and `\d` match only on ASCII characters with the respective property. |
| DOTALL, S                   | Make `.` match any character, including newlines.                                                                 |
| IGNORECASE, I               | Do case-insensitive matches.                                                                                      |
| LOCALE, L                   | Do a locale-aware match.                                                                                          |
| MULTILINE, M                | Multi-line matching, affecting `^` and `$`.                                                                       |
| VERBOSE, X (for ‘extended’) | Enable verbose REs, which can be organized more cleanly and understandably.                                       |

## More Metacharacters

`.`
&emsp; In the default mode: matches any character except a newline. If the DOTALL flag has been specified: matches any character including a newline.

`|`
&emsp; “or” operator. Example:

- `Crow|Servo` will match either `'Crow'` or `'Servo'`, not `'Cro'`, a `'w'` or an `'S'`, and `'ervo'`.

`^`
&emsp; Matches at the beginning of lines. In MULTILINE mode, also matches immediately after each newline within the string. NOTE: it behaves differently inside `[]`. Example:

```python
>>> print(re.search('^From', 'From Here to Eternity'))
<re.Match object; span=(0, 4), match='From'>
>>> print(re.search('^From', 'Reciting From Memory'))
None
```

`$`
&emsp; Matches at the end of a line or just before the newline at the end of the string, and in MULTILINE mode also matches before a newline. Example:

```python
>>> print(re.search('}$', '{block}'))
<re.Match object; span=(6, 7), match='}'>
>>> print(re.search('}$', '{block} '))
None
>>> print(re.search('}$', '{block}\n'))
<re.Match object; span=(6, 7), match='}'>
```

`\A`
&emsp; Matches only at the start of the string. When not in MULTILINE mode, `\A` and `^` are same. In MULTILINE mode: `^` may match any string that follows newline but `\A` matches only at the beginning.

`\Z`
&emsp; Matches only at the end of the string.

`\b`
&emsp; Word boundary. This is a **zero-width assertion** (These don’t cause the engine to advance through the string; meaning zero-width assertions should never be repeated, because if they match once at a given location.) that matches only at the beginning or end of a word. A word is defined as a sequence of alphanumeric characters, so the end of a word is indicated by whitespace or a non-alphanumeric character. NOTE:If you’re not using raw strings, then Python will convert the \b to a backspace. Example:

```python
>>> p = re.compile(r'\bclass\b')
>>> print(p.search('no class at all'))
<re.Match object; span=(3, 8), match='class'>
>>> print(p.search('the declassified algorithm'))
None
```

`\B`
&emsp; opposite of `\b`, only matching when the current position is not at a word boundary.

## Grouping

Groups are marked by the `'('`, `')'` metacharacters. `'('` and `')'` group together the expressions contained inside them, and you can repeat the contents of a group with a quantifier, such as `*`, `+`, `?`, or `{m,n}`. Example:

```python
>>> p = re.compile('(ab)*')
>>> print(p.match('ababababab').span())
(0, 10)
```

Group 0 is always present; it’s the whole RE, so match object methods all have group 0 as their default argument.

```python
>>> p = re.compile('(a)b')
>>> m = p.match('ab')
>>> m.group()
'ab'
>>> m.group(0)
'ab'
```

Subgroups are numbered from left to right, from 1 upward. Groups can be nested; to determine the number, just count the opening parenthesis characters, going from left to right.

```python
>>> p = re.compile('(a(b)c)d')
>>> m = p.match('abcd')
>>> m.group(0)
'abcd'
>>> m.group(1)
'abc'
>>> m.group(2)
'b'
```

group() can be passed multiple group numbers at a time, in which case it will return a tuple containing the corresponding values for those groups.

```python
>>> m.group(2,1,2)
('b', 'abc', 'b')
```

The groups() method returns a tuple containing the strings for all the subgroups, from 1 up to however many there are.

```python
>>> m.groups()
('abc', 'b')
```

**Backreferences** in a pattern allow you to specify that the contents of an earlier capturing group must also be found at the current location in the string. For example, `\1` will succeed if the exact contents of group 1 can be found at the current position, and fails otherwise. Example to detect doubled words:

```python
>>> p = re.compile(r'\b(\w+)\s+\1\b')
>>> p.search('Paris in the the spring').group()
'the the'
```

## Non-capturing and Named Groups

`(?:...)`
&emsp; non-capturing group: to use a group to denote a part of a regular expression, but aren’t interested in retrieving the group’s contents. NOTE: a non-capturing group behaves exactly like a capturing group. Example:

```python
>>> m = re.match("([abc])+", "abc")
>>> m.groups()
('c',)
>>> m = re.match("(?:[abc])+", "abc")
>>> m.groups()
()
```

`(?P<name>...)`
&emsp; named group behave exactly like capturing groups, and additionally associate a name with a group.

```python
>>> p = re.compile(r'(?P<word>\b\w+\b)')
>>> m = p.search( '(((( Lots of punctuation )))' )
>>> m.group('word')
'Lots'
```

`(?P=name)`
&emsp; indicates that the contents of the group called name should again be matched at the current point.

```python
>>> p = re.compile(r'\b(?P<word>\w+)\s+(?P=word)\b')
>>> p.search('Paris in the the spring').group()
'the the'
```

## Lookahead Assertions

`(?=...)`
&emsp; Positive lookahead assertion. This succeeds if the contained regular expression successfully matches at the current location, and fails otherwise; matching engine doesn’t advance once contained expression has been tried.

`(?!...)`
&emsp; Negative lookahead assertion. This is the opposite of the positive assertion.

## match() versus search()

match() will only report a successful match which will start at 0; if the match wouldn’t start at zero, match() will not report it while search() will scan forward through the string for a match.

```python
>>> print(re.match('super', 'superstition').span())
(0, 5)
>>> print(re.match('super', 'insuperable'))
None
>>> print(re.search('super', 'superstition').span())
(0, 5)
>>> print(re.search('super', 'insuperable').span())
(2, 7
```
