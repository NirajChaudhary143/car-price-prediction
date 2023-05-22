// function load_car_models(company_id,car_model_id)
// {
//     var company2 = document.getElementById(company_id);
//     var car_model = document.getElementById(car_model_id);
//     car_model.value="";
//     car_model.innerHTML="";

//     {% for company in companies %}

//         if(company2.value == "{{ company }}"){
         
//          {% for model in Car_model %}  
            
//             {% if company in model %}
//                 var newOption = document.createElement("option");
//                 newOption.value = "{{ model }}";
//                 newOption.innerHTML = "{{ model }}";
//                 car_model.options.add(newOption);
//             {% endif %}
          
//         {% endfor %}
//         }
//     {% endfor %}
// }