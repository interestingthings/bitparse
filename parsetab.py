
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\x0f\xe98\x81\xecnc\xab})\xe6\xa3\x9en6\x13'
    
_lr_action_items = {'UNEQUAL':([24,25,39,41,42,43,44,],[-29,-30,46,-28,-27,-25,-26,]),'LESS':([24,25,39,41,42,43,44,],[-29,-30,47,-28,-27,-25,-26,]),'MOREEQ':([24,25,39,41,42,43,44,],[-29,-30,48,-28,-27,-25,-26,]),'EQUAL':([24,25,39,41,42,43,44,],[-29,-30,49,-28,-27,-25,-26,]),'LCURLY':([4,5,40,45,],[6,-3,52,53,]),'MINUS':([23,24,25,27,39,41,42,43,44,54,55,56,57,58,59,],[34,-29,-30,34,34,-28,-27,-25,-26,34,34,34,34,34,34,]),'BITSTR':([23,24,25,41,42,43,44,],[29,-29,-30,-28,-27,-25,-26,]),'RPAREN':([22,24,25,27,38,41,42,43,44,54,55,56,57,58,59,],[28,-29,-30,40,45,-28,-27,-25,-26,-20,-22,-23,-19,-24,-21,]),'RCURLY':([6,7,8,9,10,11,13,15,16,17,28,29,32,35,36,37,52,53,60,61,62,63,],[-31,-33,-32,-5,-10,-6,21,-11,-8,-9,-16,-14,-13,-12,-15,-7,-33,-33,62,63,-18,-17,]),'PLUS':([23,24,25,27,39,41,42,43,44,54,55,56,57,58,59,],[33,-29,-30,33,33,-28,-27,-25,-26,33,33,33,33,33,33,]),'$end':([0,1,2,3,21,],[-33,0,-1,-2,-4,]),'DIVIDE':([23,24,25,27,39,41,42,43,44,54,55,56,57,58,59,],[30,-29,-30,30,30,-28,-27,-25,-26,30,30,30,30,30,30,]),'FOR':([6,7,8,9,10,11,15,16,17,28,29,32,35,36,37,52,53,60,61,62,63,],[-31,-33,12,-5,-10,-6,-11,-8,-9,-16,-14,-13,-12,-15,-7,-33,-33,12,12,-18,-17,]),'ALIGN':([6,7,8,9,10,11,15,16,17,28,29,32,35,36,37,52,53,60,61,62,63,],[-31,-33,16,-5,-10,-6,-11,-8,-9,-16,-14,-13,-12,-15,-7,-33,-33,16,16,-18,-17,]),'NUMBER':([18,20,26,30,31,33,34,46,47,48,49,50,51,],[24,24,24,24,24,24,24,24,24,24,24,24,24,]),'STUFF':([23,24,25,41,42,43,44,],[32,-29,-30,-28,-27,-25,-26,]),'UINT':([23,24,25,41,42,43,44,],[35,-29,-30,-28,-27,-25,-26,]),'LPAREN':([12,14,18,19,],[20,22,-3,26,]),'RPCHOF':([23,24,25,41,42,43,44,],[36,-29,-30,-28,-27,-25,-26,]),'TIMES':([23,24,25,27,39,41,42,43,44,54,55,56,57,58,59,],[31,-29,-30,31,31,-28,-27,-25,-26,31,31,31,31,31,31,]),'ID':([0,1,2,3,6,7,8,9,10,11,15,16,17,18,20,21,26,28,29,30,31,32,33,34,35,36,37,46,47,48,49,50,51,52,53,60,61,62,63,],[-33,5,-1,-2,-31,-33,18,-5,-10,-6,-11,-8,-9,25,25,-4,25,-16,-14,25,25,-13,25,25,-12,-15,-7,25,25,25,25,25,25,-33,-33,18,18,-18,-17,]),'IF':([6,7,8,9,10,11,15,16,17,28,29,32,35,36,37,52,53,60,61,62,63,],[-31,-33,19,-5,-10,-6,-11,-8,-9,-16,-14,-13,-12,-15,-7,-33,-33,19,19,-18,-17,]),'LESSEQ':([24,25,39,41,42,43,44,],[-29,-30,50,-28,-27,-25,-26,]),'MORE':([24,25,39,41,42,43,44,],[-29,-30,51,-28,-27,-25,-26,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'forloop':([8,60,61,],[15,15,15,]),'field':([8,60,61,],[11,11,11,]),'struct':([1,],[3,]),'ifcond':([8,60,61,],[10,10,10,]),'struct_name':([1,8,60,61,],[4,14,14,14,]),'fields':([7,52,53,],[8,60,61,]),'new_scope':([6,],[7,]),'end_scope':([8,],[13,]),'struct_list':([0,],[1,]),'type':([23,],[37,]),'struct_call':([8,60,61,],[17,17,17,]),'comparison':([26,],[38,]),'expression':([18,20,26,30,31,33,34,46,47,48,49,50,51,],[23,27,39,41,42,43,44,54,55,56,57,58,59,]),'empty':([0,7,52,53,],[2,9,9,9,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> struct_list","S'",1,None,None,None),
  ('struct_list -> empty','struct_list',1,'p_struct_list','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',42),
  ('struct_list -> struct_list struct','struct_list',2,'p_struct_list','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',43),
  ('struct_name -> ID','struct_name',1,'p_struct_name','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',52),
  ('struct -> struct_name LCURLY new_scope fields end_scope RCURLY','struct',6,'p_struct','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',57),
  ('fields -> empty','fields',1,'p_fields','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',65),
  ('fields -> fields field','fields',2,'p_fields','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',66),
  ('field -> ID expression type','field',3,'p_field','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',76),
  ('field -> ALIGN','field',1,'p_field','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',77),
  ('field -> struct_call','field',1,'p_field','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',78),
  ('field -> ifcond','field',1,'p_field','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',79),
  ('field -> forloop','field',1,'p_field','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',80),
  ('type -> UINT','type',1,'p_type','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',93),
  ('type -> STUFF','type',1,'p_type','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',94),
  ('type -> BITSTR','type',1,'p_type','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',95),
  ('type -> RPCHOF','type',1,'p_type','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',96),
  ('struct_call -> struct_name LPAREN RPAREN','struct_call',3,'p_struct_call','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',102),
  ('ifcond -> IF LPAREN comparison RPAREN LCURLY fields RCURLY','ifcond',7,'p_ifcond','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',110),
  ('forloop -> FOR LPAREN expression RPAREN LCURLY fields RCURLY','forloop',7,'p_forloop','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',115),
  ('comparison -> expression EQUAL expression','comparison',3,'p_comparison_binop','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',119),
  ('comparison -> expression UNEQUAL expression','comparison',3,'p_comparison_binop','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',120),
  ('comparison -> expression MORE expression','comparison',3,'p_comparison_binop','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',121),
  ('comparison -> expression LESS expression','comparison',3,'p_comparison_binop','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',122),
  ('comparison -> expression MOREEQ expression','comparison',3,'p_comparison_binop','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',123),
  ('comparison -> expression LESSEQ expression','comparison',3,'p_comparison_binop','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',124),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',141),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',142),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',143),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',144),
  ('expression -> NUMBER','expression',1,'p_expression_number','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',153),
  ('expression -> ID','expression',1,'p_expression_name','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',158),
  ('new_scope -> <empty>','new_scope',0,'p_new_scope','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',163),
  ('end_scope -> <empty>','end_scope',0,'p_end_scope','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',168),
  ('empty -> <empty>','empty',0,'p_empty','C:\\Users\\greenj\\Dropbox\\org\\ideas\\bitparse\\bitparse.py',173),
]
