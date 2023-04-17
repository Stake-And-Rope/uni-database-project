#!/usr/bin/python3

from PyInquirer import style_from_dict, Token


style = style_from_dict({
    Token.Separator: '#00CC00',
    Token.QuestionMark: '#00CC00 bold',
    Token.Selected: '#00CC00',  # default
    Token.Pointer: '#5F819D bold',
    Token.Instruction: '',  # default
    Token.Answer: '#5F819D bold',
    Token.Question: '',
})
