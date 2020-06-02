from negocio_fechado.models import Contract

class ContractService:
    def contractor_accept_contract(contract_pk, contractor_pk):
        contract = Contract.objects.get(pk=contract_pk)
        if int(contract.state) == 4:    
            contract.state = 5
        else:
            contract.state = 3
        contract.save()
        return contract.state
    
    def hired_accept_contract(contract_pk, hired_pk):
        contract = Contract.objects.get(pk=contract_pk)
        if int(contract.state) == 3:    
            contract.state = 5
        else:
            contract.state = 4
        contract.save()
        return contract.state
            