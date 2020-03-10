from capsul.process.xml import xml_process
import capsul_code_source as cs

@xml_process('''
<process capsul_xml="2.0">
	<input name="int1" type="int" doc=""/>
	<input name="int2" type="int" doc=""/>
	<input name="int2_0" type="int" doc=""/>
	<return name="division" type="int" doc=""/>
</process>
''')
def div_int_dyn(int1, int2, int2_0):
	listInputs=dict(zip(('int1', 'int2', 'int2_0'),(int1, int2, int2_0)))
	return cs.div_int_dyn(**listInputs).division()

@xml_process('''
<process capsul_xml="2.0">
	<input name="int1" type="int" doc=""/>
	<input name="int2" type="int" doc=""/>
	<input name="int2_0" type="int" doc=""/>
	<return name="multiplication" type="int" doc=""/>
</process>
''')
def mult_int_dyn(int1, int2, int2_0):
	listInputs=dict(zip(('int1', 'int2', 'int2_0'),(int1, int2, int2_0)))
	return cs.mult_int_dyn(**listInputs).multiplication()

@xml_process('''
<process capsul_xml="2.0">
	<input name="int1" type="int" doc=""/>
	<input name="int2" type="int" doc=""/>
	<input name="int2_0" type="int" doc=""/>
	<return name="subtract" type="int" doc=""/>
</process>
''')
def sub_int_dyn(int1, int2, int2_0):
	listInputs=dict(zip(('int1', 'int2', 'int2_0'),(int1, int2, int2_0)))
	return cs.sub_int_dyn(**listInputs).subtract()

@xml_process('''
<process capsul_xml="2.0">
	<input name="int1" type="int" doc=""/>
	<input name="int2" type="int" doc=""/>
	<input name="int2_0" type="int" doc=""/>
	<return name="addition" type="int" doc=""/>
</process>
''')
def add_int_dyn(int1, int2, int2_0):
	listInputs=dict(zip(('int1', 'int2', 'int2_0'),(int1, int2, int2_0)))
	return cs.add_int_dyn(**listInputs).addition()

@xml_process('''
<process capsul_xml="2.0">
	<input name="in1" type="float" doc=""/>
	<input name="in2" type="float" doc=""/>
	<input name="in2_0" type="float" doc=""/>
	<return name="division" type="float" doc=""/>
</process>
''')
def div_float_dyn(in1, in2, in2_0):
	listInputs=dict(zip(('in1', 'in2', 'in2_0'),(in1, in2, in2_0)))
	return cs.div_float_dyn(**listInputs).division()

@xml_process('''
<process capsul_xml="2.0">
	<input name="in1" type="float" doc=""/>
	<input name="in2" type="float" doc=""/>
	<input name="in2_0" type="float" doc=""/>
	<return name="multiplication" type="float" doc=""/>
</process>
''')
def mult_float_dyn(in1, in2, in2_0):
	listInputs=dict(zip(('in1', 'in2', 'in2_0'),(in1, in2, in2_0)))
	return cs.mult_float_dyn(**listInputs).multiplication()

@xml_process('''
<process capsul_xml="2.0">
	<input name="in1" type="float" doc=""/>
	<input name="in2" type="float" doc=""/>
	<input name="in2_0" type="float" doc=""/>
	<return name="subtract" type="float" doc=""/>
</process>
''')
def sub_float_dyn(in1, in2, in2_0):
	listInputs=dict(zip(('in1', 'in2', 'in2_0'),(in1, in2, in2_0)))
	return cs.sub_float_dyn(**listInputs).subtract()

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
	<input name="comment" type="string" doc=""/>
	<input name="inInt" type="int" doc=""/>
</process>
''')
def Print_int(comment, inInt):
	listInputs=dict(zip(('comment', 'inInt'),(comment, inInt)))
	return cs.Print_int(**listInputs)

@xml_process('''
<process capsul_xml="2.0">
	<input name="comment" type="string" doc=""/>
	<input name="inFloat" type="float" doc=""/>
</process>
''')
def Print_float(comment, inFloat):
	listInputs=dict(zip(('comment', 'inFloat'),(comment, inFloat)))
	return cs.Print_float(**listInputs)

