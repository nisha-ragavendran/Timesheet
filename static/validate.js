$(function(){
    var validateform = $("#login")
    $.validator.setDefaults({ ignore: '' });
    
    $.validator.addMethod("customrule", function(value, element, param) { 
        return this.optional(element) || value === param; 
      }, "Total working hours should be {0}!");

    validateform.validate({
        rules:{
            User:{
                required: true
            },
            Date:{
                required: true
            },
            counter:{
                required:true,
                customrule:8
            }
        },
        messages:{
            User:{
                required: 'Please enter Username'
            },
            Date:{
                required: 'Please enter Date'
            }
        }
    })
})