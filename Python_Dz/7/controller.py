import wr_file
import view
import rd_file


data = view.data_input()
wr_file.write_file(data)
rd_file.read_file()