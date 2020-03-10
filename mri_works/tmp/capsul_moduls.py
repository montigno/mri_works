from capsul.process.xml import xml_process
import capsul_code_source as cs

@xml_process('''
<process capsul_xml="2.0">
	<input name="x" type="float" doc=""/>
	<input name="y" type="float" doc=""/>
	<return name="out" type="bool" doc=""/>
</process>
''')
def x_Equal_y(x, y):
	listInputs=dict(zip(('x', 'y'),(x, y)))
	return cs.x_Equal_y(**listInputs).out()

@xml_process('''
<process capsul_xml="2.0">
	<input name="x" type="float" doc=""/>
	<input name="y" type="float" doc=""/>
	<return name="out" type="bool" doc=""/>
</process>
''')
def x_GreaterOrEqual_y(x, y):
	listInputs=dict(zip(('x', 'y'),(x, y)))
	return cs.x_GreaterOrEqual_y(**listInputs).out()

@xml_process('''
<process capsul_xml="2.0">
	<input name="x" type="float" doc=""/>
	<input name="y" type="float" doc=""/>
	<return name="out" type="bool" doc=""/>
</process>
''')
def x_Greater_y(x, y):
	listInputs=dict(zip(('x', 'y'),(x, y)))
	return cs.x_Greater_y(**listInputs).out()

@xml_process('''
<process capsul_xml="2.0">
	<input name="x" type="float" doc=""/>
	<input name="y" type="float" doc=""/>
	<return name="out" type="bool" doc=""/>
</process>
''')
def x_LessOrEqual_y(x, y):
	listInputs=dict(zip(('x', 'y'),(x, y)))
	return cs.x_LessOrEqual_y(**listInputs).out()

@xml_process('''
<process capsul_xml="2.0">
	<input name="x" type="float" doc=""/>
	<input name="y" type="float" doc=""/>
	<return name="out" type="bool" doc=""/>
</process>
''')
def x_Less_y(x, y):
	listInputs=dict(zip(('x', 'y'),(x, y)))
	return cs.x_Less_y(**listInputs).out()

@xml_process('''
<process capsul_xml="2.0">
	<input name="x" type="float" doc=""/>
	<input name="y" type="float" doc=""/>
	<return name="out" type="bool" doc=""/>
</process>
''')
def x_Not_Equal_y(x, y):
	listInputs=dict(zip(('x', 'y'),(x, y)))
	return cs.x_Not_Equal_y(**listInputs).out()

@xml_process('''
<process capsul_xml="2.0">
	<input name="comment" type="string" doc=""/>
	<input name="inBool" type="bool" doc=""/>
</process>
''')
def Print_bool(comment, inBool):
	listInputs=dict(zip(('comment', 'inBool'),(comment, inBool)))
	return cs.Print_bool(**listInputs)

