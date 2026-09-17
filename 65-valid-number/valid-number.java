class Solution {
    private static final Set<String> INVALID_STRINGS = Set.of(
        "nan", "inf", "+inf", "-inf",
        "Infinity", "+Infinity", "-Infinity"
    );
    public boolean isNumber(String s) {
        if (s==null || INVALID_STRINGS.contains(s))return false;
        char lastChar=s.charAt(s.length()-1);
        if (lastChar == 'f' || lastChar == 'F' || lastChar == 'd' || lastChar == 'D') {
            return false;
        }
        try{
            Double.parseDouble(s);
            return true;
        }
        catch (NumberFormatException e){
            return false;
        }
    }
}