/*
	Este script recorre una lista dos veces ordenando de menor a mayor sus elementos
*/
function func(ls) {
	const N = ls.length; 						
	for (let i = 0; i < N ; i++) { 				
		let flag = true;						
		for(let j = 0 ; j < N - i - 1; j++){	
			if (ls[j] > ls[j + 1]) {			
				flag = false
				const aux = ls[j];
				ls[j] = ls[j+1];
				ls[j + 1] = aux;
			}
		}
		if(flag){
			break
		}
	}
	return ls;
}
