from capsul.process.xml import xml_process
import capsul_code_source as cs

@xml_process('''
<process capsul_xml="2.0">
	<input name="comment" type="string" doc=""/>
	<input name="inFloat" type="float" doc=""/>
</process>
''')
def Print_Float(comment, inFloat):
	listInputs=dict(zip(('comment', 'inFloat'),(comment, inFloat)))
	return cs.Print_Float(**listInputs)

@xml_process('''
<process capsul_xml="2.0">
	<input name="x" type="float" doc=""/>
	<input name="out_angle_type" type="string" doc=""/>
	<return name="arcsinus" type="float" doc=""/>
</process>
''')
def numpy_arcsin(x, out_angle_type):
	listInputs=dict(zip(('x', 'out_angle_type'),(x, out_angle_type)))
	return cs.numpy_arcsin(**listInputs).arcsinus()

@xml_process('''
<process capsul_xml="2.0">
	<input name="x" type="float" doc=""/>
	<input name="angle_type" type="string" doc=""/>
	<return name="sinus" type="float" doc=""/>
</process>
''')
def numpy_sin(x, angle_type):
	listInputs=dict(zip(('x', 'angle_type'),(x, angle_type)))
	return cs.numpy_sin(**listInputs).sinus()

@xml_process('''
<process capsul_xml="2.0">
	<input name="x" type="float" doc=""/>
	<input name="out_angle_type" type="string" doc=""/>
	<return name="arccosinus" type="float" doc=""/>
</process>
''')
def numpy_arccos(x, out_angle_type):
	listInputs=dict(zip(('x', 'out_angle_type'),(x, out_angle_type)))
	return cs.numpy_arccos(**listInputs).arccosinus()

@xml_process('''
<process capsul_xml="2.0">
	<input name="x" type="float" doc=""/>
	<input name="angle_type" type="string" doc=""/>
	<return name="cosinus" type="float" doc=""/>
</process>
''')
def numpy_cos(x, angle_type):
	listInputs=dict(zip(('x', 'angle_type'),(x, angle_type)))
	return cs.numpy_cos(**listInputs).cosinus()

@xml_process('''
<process capsul_xml="2.0">
	<input name="x" type="float" doc=""/>
	<input name="angle_type" type="string" doc=""/>
	<return name="tan" type="float" doc=""/>
</process>
''')
def numpy_tan(x, angle_type):
	listInputs=dict(zip(('x', 'angle_type'),(x, angle_type)))
	return cs.numpy_tan(**listInputs).tan()

@xml_process('''
<process capsul_xml="2.0">
	<input name="x" type="float" doc=""/>
	<input name="out_angle_type" type="string" doc=""/>
	<return name="arctan" type="float" doc=""/>
</process>
''')
def numpy_arctan(x, out_angle_type):
	listInputs=dict(zip(('x', 'out_angle_type'),(x, out_angle_type)))
	return cs.numpy_arctan(**listInputs).arctan()

