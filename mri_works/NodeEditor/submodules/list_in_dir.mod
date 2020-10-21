[diagram]
constant=[A1] value=['*.nii'] format=[str] label=[filter] RectF=[(-850.104887143375, -65.06563837525701, 53.0, 33.0)]
constant=[A2] value=['True'] format=[bool] label=[recursive] RectF=[(-764.6731349745503, 20.366131157225468, 79.0, 31.0)]
link=[N1] node=[C0:RepDefault#Node#U13:RepDefault]
link=[N0] node=[U0:list_out#Node#U1:in_list_Path]
link=[N11] node=[U13:listFiles#Node#U0:files_list]
link=[N19] node=[A1:#Node#U13:filter]
link=[N27] node=[A2:#Node#U13:recursive]
connt=[C0] name=[RepDefault] type=[in] format=[path] valOut=[path] RectF=[(-791.155867425312, -187.50699097283473, 70, 24)]
block=[U1] category=[Tools.Print] class=[Print_list_path] valInputs=[(['comment', 'in_list_Path'], ['', 'Node(N0)'], [], [])] RectF=[(-41.08319096822345, -72.4998519292813, 150.0, 80.0)]
block=[U13] category=[File_IO.Dialog_files_directories] class=[list_files_in_directory] valInputs=[(['RepDefault', 'title', 'filter', 'recursive'], ['Node(N1)', 'Select a directory', 'Node(N19)', 'Node(N27)'], ['listFiles'], ['list_path'])] RectF=[(-567.9365052101673, -110.06502014097595, 158.328125, 120.2043785309045)]
block=[U0] category=[Tools.PathManipulation] class=[order_name_files] valInputs=[(['files_list', 'reverse'], ['Node(N11)', False], ['list_out'], ['list_path'])] RectF=[(-302.08184607465114, -81.4174124561614, 150.0, 80.0)]
[execution]
['C0:RepDefault=']
['U13', 'U0', 'U1']
{'U0': ('Tools.PathManipulation', 'order_name_files', "(['files_list', 'reverse'], ['U13:listFiles', False], ['list_out'], ['list_path'])"), 'U1': ('Tools.Print', 'Print_list_path', "(['comment', 'in_list_Path'], ['', 'U0:list_out'], [], [])"), 'U13': ('File_IO.Dialog_files_directories', 'list_files_in_directory', "(['RepDefault', 'title', 'filter', 'recursive'], ['C0:RepDefault', 'Select a directory', '*.nii', True], ['listFiles'], ['list_path'])")}
['A2:', 'A1:', 'U13:listFiles', 'U0:list_out', 'C0:RepDefault']
{}
[]