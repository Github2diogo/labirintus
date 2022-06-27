function limpaAcentos(umaString){

    // console.log(umaString);
    
    umaString = umaString.replaceAll('â', 'a');
    umaString = umaString.replaceAll('á', 'a');

    umaString = umaString.replaceAll('é', 'e');
    umaString = umaString.replaceAll('ê', 'e');
    
    umaString = umaString.replaceAll('í', 'i');
    
    umaString = umaString.replaceAll('ó', 'o');
    umaString = umaString.replaceAll('ô', 'o');
    
    umaString = umaString.replaceAll('ç', 'c');
    umaString = umaString.replaceAll(',', '');
    
    umaString = umaString.replaceAll(' da ', ' ');
    umaString = umaString.replaceAll(' de ', ' ');
    umaString = umaString.replaceAll(' e ', ' ');
    umaString = umaString.replaceAll(' do ', ' ');
    
    umaString = umaString.replaceAll('&nbsp;', ' ');
    umaString = umaString.replaceAll(' - ', ' ');
    umaString = umaString.replaceAll('; ', ' ');
    umaString = umaString.replaceAll(', ', ' ');
    
    // console.log(umaString);

    return umaString
}

function filtraLista() {
  
    var buscaDigitada, busca, ul, li, a, n;
    
    buscaDigitada = document.getElementById("caixaDeBusca");
    busca = buscaDigitada.value.toLowerCase();
    
    if (busca == 'lme'){ busca = "lab metrologia elétrica";}
    if (busca == 'lmm'){ busca = "lab metrologia mecanica";}
    
    // dicas
    dicas(busca);

    // pros casos de p junto com o número
    if(busca[0] == 'p' && isNaN(busca[1]) == false && busca[1] != 0 && isNaN(busca[2]) == true ){
        n = busca[1]
        busca = busca.replace(n, '0'+n);
        busca = busca.replace('p', 'p ');
    }
    
    // pros casos de p separado do número e com prédios menores que 10
    if(busca[0] == 'p' && busca[1] == ' ' && busca.length == 3){
        n = busca[2]
        busca = busca.replace(n, '0'+n);
    }

    // pros casos prédio maior que 10 e p separado
    if(busca.length == 3 && busca[0] == 'p' && isNaN(busca[1]) == false && isNaN(busca[2]) == false){
        busca = busca.replace('p', 'p ');
    }


    busca = busca.replace('lab ', 'laboratorio ');
    busca = busca.replace('p ', 'prédio ');


    busca = limpaAcentos(busca);

    console.log(busca);

    if (busca.length > 1){
        
        ul = document.getElementById("listaDosPredios"); // a lista completa
        li = ul.getElementsByTagName("li"); // um elemento da lista
        
        for (var i = 0; i < li.length; i++) {
            
            a = li[i].getElementsByTagName('a')[0]; //cada um dos elementos com a tag 'a' começando pelo primeiro
            // console.log(a)
            b = a.innerHTML.toLowerCase();
            b = limpaAcentos(b);

            if (b.search(busca) > -1) {
                li[i].style.display = "";
            }
            else {
                li[i].style.display = "none";
            }
        }
    
    } else {
        
        ul = document.getElementById("listaDosPredios"); // a lista completa
        li = ul.getElementsByTagName("li"); // um elemento da lista
        
        for (var i = 0; i < li.length; i++) {    
            li[i].style.display = "none";
        }
    }
}

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