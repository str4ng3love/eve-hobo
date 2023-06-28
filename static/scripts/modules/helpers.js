export function AllowOnlyDigits(e){
    if(e.data == null){
        return false
    }
    if(e.data.match(/[0-9]/)){
        return true
    }else {
        return false
    }
}   