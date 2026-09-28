import lseg.data as ld

ld.open_session()
print(ld.get_data("IBM.N", ["TR.PriceClose"]))
ld.close_session()
