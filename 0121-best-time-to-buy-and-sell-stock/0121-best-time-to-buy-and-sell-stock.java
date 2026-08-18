class Solution {
    public int maxProfit(int[] prices) {
        int min_price=prices[0];
        int maxp=0;

        for(int i=1; i<=prices.length-1;i++){
            if(prices[i]< min_price){
                min_price=prices[i];
            }
            int profit =prices[i]- min_price;
            if(profit>maxp){
                maxp=profit;
            }
        }
        return maxp;
    }
}