from Usuario import Usuario

gaby = Usuario("Gaby")
martha = Usuario ("Martha")
cilo = Usuario ("Cilo")

gaby.balance_cuenta=0
martha.balance_cuenta=0
cilo.balance_cuenta=0

gaby.hacer_deposito(100).hacer_deposito(20).hacer_deposito(30).hacer_retiro(5).mostrar_balance_usuario()
martha.hacer_deposito(1000).hacer_retiro(50).hacer_retiro(40).mostrar_balance_usuario()
cilo.hacer_deposito(2000).hacer_retiro(500).hacer_retiro(300).mostrar_balance_usuario()

gaby.transfer_dinero(cilo, 5)
martha.transfer_dinero(gaby, 15)
cilo.transfer_dinero(gaby,10)
