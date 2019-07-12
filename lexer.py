#
# Copyright (c) 2019 Vijay Kumar Banerjee <vijaykumar9597@gmail.com> 
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

from constant import *

def lex_string(string):
  
  json_string = ''
  
  if string[0] == QUOTE:
    string = string[1:]
  else:
    return None, string
  
  for c in string:
    if c == QUOTE:
      return json_string, string[len(json_string)+1:]

    else:
      json_string += c
  
  raise Exception('End of string quote missing')

def lex_number(string):
  json_number = ''

  number_characters = [str(d) for d in range(0, 10)] + ['-', 'e', '.']

  for c in string:
      if c in number_characters:
          json_number += c
      else:
          break

  rest = string[len(json_number):]

  if not len(json_number):
      return None, string

  if '.' in json_number:
      return float(json_number), rest

  return int(json_number), rest

def lex_null(string):
  strlen = len(string)

  if strlen >= NULL_LEN and string[:NULL_LEN] == 'null':
    return True, string[NULL_LEN]

  return None, string

def lex_bool(string):
  string_len = len(string)

  if string_len >= TRUE_LEN and \
     string[:TRUE_LEN] == 'true':
    return True, string[TRUE_LEN:]
  elif string_len >= FALSE_LEN and \
       string[:FALSE_LEN] == 'false':
    return False, string[FALSE_LEN:]

  return None, string

def lex(string):
  tokens = []

  while len(string):

    json_string, string = lex_string(string)
    if json_string is not None:
      tokens.append(json_string)
      continue

    json_number, string = lex_number(string)
    if json_number is not None:
      tokens.append(json_number)
      continue

    json_null, string = lex_null(string)
    if json_null is not None:
      tokens.append(None)
      continue

    if string[0] in WHITESPACE:
      string = string[1:]

    elif string[0] in SYNTAX:
      tokens.append(string[0])
      string = string[1:]

    else:
      raise Exception("Unknown character: {}".format(string[0]))

  return tokens
