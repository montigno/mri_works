from capsul.process.xml import xml_process
import capsul_code_source as cs

@xml_process('''
<process capsul_xml="2.0">
	<input name="comment" type="string" doc=""/>
	<input name="inFloat" type="float" doc=""/>
</process>
''')
def Print_float(comment, inFloat):
	listInputs=dict(zip(('comment', 'inFloat'),(comment, inFloat)))
	return cs.Print_float(**listInputs)

@xml_process('''
<process capsul_xml="2.0">
	<input name="in1" type="float" doc=""/>
	<input name="in2" type="float" doc=""/>
	<input name="in2_0" type="float" doc=""/>
	<return name="addition" type="float" doc=""/>
</process>
''')
def add_float_dyn(in1, in2, in2_0):
	listInputs=dict(zip(('in1', 'in2', 'in2_0'),(in1, in2, in2_0)))
	return cs.add_float_dyn(**listInputs).addition()

@xml_process('''
<process capsul_xml="2.0">
	<input name="in1" type="float" doc=""/>
	<input name="in2" type="float" doc=""/>
	<return name="subtract" type="float" doc=""/>
</process>
''')
def sub_float_dyn(in1, in2):
	listInputs=dict(zip(('in1', 'in2'),(in1, in2)))
	return cs.sub_float_dyn(**listInputs).subtract()

@xml_process('''
<process capsul_xml="2.0">
	<input name="in1" type="float" doc=""/>
	<input name="in2" type="float" doc=""/>
	<return name="multiplication" type="float" doc=""/>
</process>
''')
def mult_float_dyn(in1, in2):
	listInputs=dict(zip(('in1', 'in2'),(in1, in2)))
	return cs.mult_float_dyn(**listInputs).multiplication()

