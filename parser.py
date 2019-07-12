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
import lexer

def parse_array(tokens):
    json_array = []

    t = tokens[0]
    if t == JSON_RIGHTBRACKET:
        return json_array, tokens[1:]

    while True:
        json, tokens = parse(tokens)
        json_array.append(json)

        t = tokens[0]
        if t == JSON_RIGHTBRACKET:
            return json_array, tokens[1:]
        elif t != JSON_COMMA:
            raise Exception('Expected comma after object in array')
        else:
            tokens = tokens[1:]

    raise Exception('Expected end-of-array bracket')

def parse_object(tokens):
  json_object = {}
  t = tokens[0]

  if t == JSON_RIGHTBRACE:
    return json_object, tokens[1:]
  
  while True:
    json_key = tokens[0]

    if type(json_key) is str:
      tokens = tokens[1:]
    else:
      raise Exception ('Expected key of type string')

    if tokens[0] != JSON_COLON:
      raise Exception ('Expected colol ( : ) in object type dict')
    else:
      tokens = tokens[1:]

    json_value, tokens = parse(tokens)
    json_object[json_key] = json_value

    t = tokens[0]
    if t == JSON_RIGHTBRACE:
      return json_object, tokens[1:]
    elif t != JSON_COMMA:
      raise Exception('Expected comma after pair in object, got: {}'.format(t))
    tokens = tokens[1:]
  
  raise Exception('Expected end-of-object brace')

def parse(tokens):
  
  t = tokens[0]

  if t == JSON_LEFTBRACKET:
    return parse_array(tokens[1:])
  
  elif t == JSON_LEFTBRACE:
    return parse_object(tokens[1:])
  
  else:
    return t, tokens[1:]
  
