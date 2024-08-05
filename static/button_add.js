$(document).ready(function() {
    $("#btnAdd").click(function(){
        var id = $('table tr').length - 1,
        count = $('table tr').length,
        totalSum = 0,
        i,
        row = '<tr>';
          row += '<td><input type="text" id="text_'+id+'_P" name="text_'+id+'_P" />'
          row += '<td><input type="text" id="text_'+id+'_T" name="text_'+id+'_T" size="160"/>'
          row += '<td><input type="text" class="hours" id="text_'+id+'_H" name="text_'+id+'_H" />'
        row += '</tr>';
         
         $('table').append(row);
        
         
         $('#counter').val(count);

         var sum = 0;  
         $('.hours').each(function() {
          sum += +$(this).val();
           $('#totalhours').val(sum);

        if(sum > 8){
          $('.err').show();
          return false;
        }
        else{
          $('.err').hide();
          return true;
        }
    });
  });
    
    
    
  
  });

  
 
     

