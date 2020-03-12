from capsul.process.xml import xml_process
import capsul_code_source as cs

@xml_process('''
<process capsul_xml="2.0">
	<input name="list_in_str" type="list_string" doc=""/>
	<input name="index" type="int" doc=""/>
	<return name="out_list_indexed" type="string" doc=""/>
</process>
''')
def index_list_str(list_in_str, index):
	listInputs=dict(zip(('list_in_str', 'index'),(list_in_str, index)))
	return cs.index_list_str(**listInputs).out_list_indexed()

@xml_process('''
<process capsul_xml="2.0">
	<input name="nii_image" type="file" doc=""/>
	<input name="structarr" type="string" doc=""/>
	<return name="out_structarr" type="list_string" doc=""/>
</process>
''')
def Nifti_rawInfo(nii_image, structarr):
	listInputs=dict(zip(('nii_image', 'structarr'),(nii_image, structarr)))
	return cs.Nifti_rawInfo(**listInputs).out_structarr()

@xml_process('''
<process capsul_xml="2.0">
	<input name="command" type="string" doc=""/>
</process>
''')
def ImageJ_execution(command,):
	listInputs=dict(zip(('command',),(command,)))
	return cs.ImageJ_execution(**listInputs)

@xml_process('''
<process capsul_xml="2.0">
	<input name="cmd_ant" type="string" doc=""/>
	<input name="coord" type="list_int" doc=""/>
	<return name="cmd_post" type="string" doc=""/>
</process>
''')
def Plot_profil(cmd_ant, coord):
	listInputs=dict(zip(('cmd_ant', 'coord'),(cmd_ant, coord)))
	return cs.Plot_profil(**listInputs).cmd_post()

@xml_process('''
<process capsul_xml="2.0">
	<input name="file" type="file" doc=""/>
	<return name="cmd_post" type="string" doc=""/>
</process>
''')
def ImageJ_load_Image(file,):
	listInputs=dict(zip(('file',),(file,)))
	return cs.ImageJ_load_Image(**listInputs).cmd_post()

@xml_process('''
<process capsul_xml="2.0">
	<input name="int_in" type="int" doc=""/>
	<input name="int_in_0" type="int" doc=""/>
	<input name="int_in_1" type="int" doc=""/>
	<input name="int_in_2" type="int" doc=""/>
	<return name="out_list" type="list_int" doc=""/>
</process>
''')
def build_list_int_dyn(int_in, int_in_0, int_in_1, int_in_2):
	listInputs=dict(zip(('int_in', 'int_in_0', 'int_in_1', 'int_in_2'),(int_in, int_in_0, int_in_1, int_in_2)))
	return cs.build_list_int_dyn(**listInputs).out_list()

@xml_process('''
<process capsul_xml="2.0">
	<input name="int1" type="int" doc=""/>
	<input name="int2" type="int" doc=""/>
	<return name="division" type="int" doc=""/>
</process>
''')
def div_int_dyn(int1, int2):
	listInputs=dict(zip(('int1', 'int2'),(int1, int2)))
	return cs.div_int_dyn(**listInputs).division()

@xml_process('''
<process capsul_xml="2.0">
	<input name="extension" type="string" doc=""/>
	<input name="title" type="string" doc=""/>
	<return name="filePath" type="file" doc=""/>
</process>
''')
def askopenfilename(extension, title):
	listInputs=dict(zip(('extension', 'title'),(extension, title)))
	return cs.askopenfilename(**listInputs).filePath()

@xml_process('''
<process capsul_xml="2.0">
	<input name="inString" type="string" doc=""/>
	<return name="outInt" type="int" doc=""/>
</process>
''')
def StringToInt(inString,):
	listInputs=dict(zip(('inString',),(inString,)))
	return cs.StringToInt(**listInputs).outInt()

