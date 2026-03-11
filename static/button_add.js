$(document).ready(function () {
  function updateTotalHours() {
    var sum = 0;

    $(".hours").each(function () {
      var value = parseFloat($(this).val());
      if (!Number.isNaN(value)) {
        sum += value;
      }
    });

    $("#totalhours").val(sum);

    if (sum > 8) {
      $(".err").show();
    } else {
      $(".err").hide();
    }
  }

  $("#btnAdd").on("click", function () {
    var id = $("table tr").length - 1;
    var row = "<tr>";
    row += '<td><input type="text" id="text_' + id + '_P" name="text_' + id + '_P" /></td>';
    row += '<td><input type="text" id="text_' + id + '_T" name="text_' + id + '_T" size="160" /></td>';
    row += '<td><input type="text" class="hours" id="text_' + id + '_H" name="text_' + id + '_H" /></td>';
    row += "</tr>";

    $("table").append(row);
    $("#counter").val(id + 1);
    updateTotalHours();
  });

  $(document).on("input", ".hours", updateTotalHours);
  updateTotalHours();
});
