CSS: style.css
dnl
define(reqdef,`
{#$1}$1
: $2 

[$1]: #$1 "$2"')dnl
dnl
dnl
dnl
define(tcPF,`
<form>
<fieldset>
<legend>Results for Test Case $1</legend>
<input type="radio" name="tc$1" value="Pass" id="tc$1Pass" checked="false"/>
<label for="Pass">Pass</label>
<input type="radio" name="tc$1" value="Fail" id="tc$1Fail" checked="false"/>
<label for="Fail">Fail</label>
<input type="radio" name="tc$1" value="Skip" id="tc$1Skip" checked="true"/>
<label for="Skip">Skip</label>
<input type="submit" name="tc$1" value="Save" id="tc$1Save" />
</fieldset>
</form>')dnl
dnl
dnl
dnl
include(title.md)dnl
include(requirements.md)dnl
include(testcases.md)dnl
include(signature.md)dnl
