function dicas(busca){
    
    var elem = document.getElementById('caixaDeDicas');
    
    if(busca[0] == 'p'){
        elem.innerHTML = 'Dica: para achar um prédio você pode digitar apenas "p" e o número do prédio'
    } else { 
        if(busca.search('lab') > -1 && busca.length <= 12){
            elem.innerHTML = 'Dica: você pode escrever apenas "lab" para achar um laboratório'
        } else {
            if(isNaN(busca) == false && busca.length > 1){
                elem.innerHTML = 'Dica: se estiver buscando um prédio e não um ramal, tente usar "p" antes do número'
            } else { 
                if(!busca == true){
                    elem.innerHTML = '[[][][][][][][]]'
                } else {
                    elem.innerHTML = 'Dica: você pode buscar pela sigla do laboratório / seção / departamento'
                }
            }
        }
    }
}
