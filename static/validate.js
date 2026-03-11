$(function () {
  var validateForm = $("#login");
  $.validator.setDefaults({ ignore: "" });

  $.validator.addMethod(
    "exacttotal",
    function (value, element, param) {
      if (this.optional(element)) {
        return true;
      }
      return Number(value) === param;
    },
    "Total working hours should be {0}."
  );

  validateForm.validate({
    rules: {
      User: {
        required: true,
      },
      Date: {
        required: true,
      },
      totalhours: {
        required: true,
        exacttotal: 8,
      },
      text_0_H: {
        required: true,
        number: true,
      },
    },
    messages: {
      User: {
        required: "Please enter username.",
      },
      Date: {
        required: "Please enter date.",
      },
      totalhours: {
        required: "Please enter hours.",
      },
      text_0_H: {
        required: "Please enter hours.",
        number: "Hours must be numeric.",
      },
    },
  });
});
