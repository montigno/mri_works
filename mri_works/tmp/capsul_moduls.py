from capsul.process.xml import xml_process
import capsul_code_source as cs

@xml_process('''
<process capsul_xml="2.0">
	<input name="comment" type="string" doc=""/>
	<input name="inPath" type="file" doc=""/>
</process>
''')
def Print_Path(comment, inPath):
	listInputs=dict(zip(('comment', 'inPath'),(comment, inPath)))
	return cs.Print_Path(**listInputs)

@xml_process('''
<process capsul_xml="2.0">
	<input name="comment" type="string" doc=""/>
	<input name="in_list_Path" type="list_file" doc=""/>
</process>
''')
def Print_list_Path(comment, in_list_Path):
	listInputs=dict(zip(('comment', 'in_list_Path'),(comment, in_list_Path)))
	return cs.Print_list_Path(**listInputs)

@xml_process('''
<process capsul_xml="2.0">
	<input name="input_image" type="file" doc=""/>
	<input name="save_bias" type="bool" doc=""/>
	<input name="copy_header" type="bool" doc=""/>
	<return>
		<output name="output_image" type="file" doc=""/>
		<output name="bias_image" type="file" doc=""/>
	</return>
</process>
''')
def ants_N4BiasFieldCorrection(input_image, save_bias, copy_header):
	listInputs=dict(zip(('input_image', 'save_bias', 'copy_header'),(input_image, save_bias, copy_header)))
	z=cs.ants_N4BiasFieldCorrection(**listInputs)
	return {
		'output_image': z.output_image(),
		'bias_image': z.bias_image(),
	}

@xml_process('''
<process capsul_xml="2.0">
	<input name="in_files" type="file" doc=""/>
	<return>
		<output name="tissue_class_map" type="file" doc=""/>
		<output name="tissue_class_files" type="list_file" doc=""/>
		<output name="restored_image" type="list_file" doc=""/>
		<output name="mixeltype" type="file" doc=""/>
		<output name="partial_volume_map" type="file" doc=""/>
		<output name="partial_volume_files" type="list_file" doc=""/>
		<output name="bias_field" type="list_file" doc=""/>
		<output name="probability_maps" type="list_file" doc=""/>
	</return>
</process>
''')
def fsl_FAST(in_files,):
	listInputs=dict(zip(('in_files',),(in_files,)))
	z=cs.fsl_FAST(**listInputs)
	return {
		'tissue_class_map': z.tissue_class_map(),
		'tissue_class_files': z.tissue_class_files(),
		'restored_image': z.restored_image(),
		'mixeltype': z.mixeltype(),
		'partial_volume_map': z.partial_volume_map(),
		'partial_volume_files': z.partial_volume_files(),
		'bias_field': z.bias_field(),
		'probability_maps': z.probability_maps(),
	}

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

