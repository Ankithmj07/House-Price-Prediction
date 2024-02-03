/*var defaultButton=''
defaultButton='<a href="#" class="button button--flex button--small button-predict" id="predict-button" onclick="validateForm()">Predict<i class="uil uil-angle-right button__icon"></i></a>'

document.getElementById('changeButton').innerHTML=defaultButton

newButton='<a href="#" class="button button--flex button--small button-predict" data-bs-toggle="modal" data-bs-target="#predictModal" id="predict-button">new<i class="uil uil-angle-right button__icon"></i></a>'*/


const predictButton = document.getElementById('predict-button')
function validateForm(){

    var numberPattern = /^\d*\.?\d+$/;
    var longitude = document.getElementById('longitude').value
    

    if(longitude==''){
        document.getElementById('errMsgLongitude').innerHTML='Please Enter longitude'
        return false
    }
    else{
        document.getElementById('errMsgLongitude').innerHTML=''
        var longitudePattern=/-\d*\.?\d+$/;

        if(longitudePattern.test(longitude)){
            document.getElementById('errMsgLongitude').innerHTML=''
        }
       else{
            document.getElementById('errMsgLongitude').innerHTML='Please enter valid longitude'
            return false
       }
    }   

    var latitude = document.getElementById('latitude').value

    if(latitude==''){
        document.getElementById('errMsgLatitude').innerHTML='Please Enter latitude'
        return false
    }
    else{
        document.getElementById('errMsgLatitude').innerHTML=''

        if(numberPattern.test(latitude)){
            document.getElementById('errMsgLatitude').innerHTML=''
        }
       else{
            document.getElementById('errMsgLatitude').innerHTML='Please enter valid latitude'
            return false
       }
    }   

    var medianAge = document.getElementById('house_age').value

    if(medianAge==''){
        document.getElementById('errMsgMedianAge').innerHTML='Please Enter housing median age'
        return false
    }
    else{
        document.getElementById('errMsgMedianAge').innerHTML=''

        if(numberPattern.test(medianAge)){
            document.getElementById('errMsgMedianAge').innerHTML=''
        }
       else{
            document.getElementById('errMsgMedianAge').innerHTML='Please enter valid housing median age'
            return false
       }
    }   

    var totalRooms = document.getElementById('total_rooms').value

    if(totalRooms==''){
        document.getElementById('errMsgRooms').innerHTML='Please Enter total no. of rooms'
        return false
    }
    else{
        document.getElementById('errMsgRooms').innerHTML=''

        if(numberPattern.test(totalRooms)){
            document.getElementById('errMsgRooms').innerHTML=''
        }
       else{
            document.getElementById('errMsgRooms').innerHTML='Please enter valid total rooms'
            return false
       }
    }   

    var totalBedrooms = document.getElementById('total_bedrooms').value

    if(totalBedrooms==''){
        document.getElementById('errMsgBedrooms').innerHTML='Please Enter total no. of bed rooms'
        return false
    }
    else{
        document.getElementById('errMsgBedrooms').innerHTML=''

        if(numberPattern.test(totalBedrooms)){
            document.getElementById('errMsgBedrooms').innerHTML=''
        }
       else{
            document.getElementById('errMsgBedrooms').innerHTML='Please enter valid total bed rooms'
            return false
       }
    }   

    var population = document.getElementById('population').value

    if(population==''){
        document.getElementById('errMsgPopulation').innerHTML='Please Enter population'
        return false
    }
    else{
        document.getElementById('errMsgPopulation').innerHTML=''

        if(numberPattern.test(population)){
            document.getElementById('errMsgPopulation').innerHTML=''
        }
       else{
            document.getElementById('errMsgPopulation').innerHTML='Please enter valid population'
            return false
       }
    }    

    var households = document.getElementById('households').value

    if(households==''){
        document.getElementById('errMsgHouseholds').innerHTML='Please Enter housholds'
        return false
    }
    else{
        document.getElementById('errMsgHouseholds').innerHTML=''

        if(numberPattern.test(households)){
            document.getElementById('errMsgHouseholds').innerHTML=''
        }
       else{
            document.getElementById('errMsgHouseholds').innerHTML='Please enter valid households'
            return false
       }
    }      
    
    var income = document.getElementById('income').value

    if(income==''){
        document.getElementById('errMsgIncome').innerHTML='Please Enter income'
        return false
    }
    else{
        document.getElementById('errMsgIncome').innerHTML=''

        if(numberPattern.test(income)){
            document.getElementById('errMsgIncome').innerHTML=''
        }
       else{
            document.getElementById('errMsgIncome').innerHTML='Please enter valid income'
            return false
       }
    }     

    var oceanProximity=document.getElementById('ocean').value
    
    if(oceanProximity=='choose'){
        document.getElementById('errMsgOcean').innerHTML='Please choose an ocean proximity'
        return false
    }
    else{
        document.getElementById('errMsgOcean').innerHTML=''
    }

    var xhttpsendDetails=new XMLHttpRequest()
    xhttpsendDetails.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200)     //200(Success), 300(Redirect), 400(server not found), 500(Internal server error)
        {
            console.log(this.responseText)
            var jsonData=JSON.parse(this.responseText)
            
            localStorage.setItem('predictedPrice', JSON.stringify(jsonData));
            console.log(localStorage.getItem('predictedPrice'))
            
            window.location.href='/Prediction'
            
        }
        

    }
    xhttpsendDetails.open("POST","http://127.0.0.1:8081/send-details",true)
    xhttpsendDetails.setRequestHeader("Content-type","application/x-www-form-urlencoded")
    xhttpsendDetails.send('longitude='+longitude+'&latitude='+latitude+'&medianAge='+medianAge+'&totalRooms='+totalRooms+'&totalBedrooms='+totalBedrooms+'&population='+population+'&households='+households+'&income='+income+'&oceanProximity='+oceanProximity)
    
}









