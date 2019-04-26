# Find best trade from a given set of trading prices per second.
# Memory efficient and fastest method for finding best trade prices.

#
# Takes n for loops and n*4 if loops for calculation.
# Ran with 64Kib and 0.0105sec on Hackerearth for 50k random records.

# Holding individual spike blocks.
Blocks = []

class Block:
    """
    Managing individual block of spike.
    """
    def __init__(self, start):
        self.start = start
    def updateEnd(self, end):
        self.end = end
    def margin(self):
        return self.end - self.start

def GetMaxProfit(dataset):
    min = dataset[0]
    max = dataset[0]

    block = None
    for price in dataset:
        # Max is increasing our profits are going up.
        if price > max:
            max = price
            # Start a new block we are in a spike.
            if block is None:
                block = Block(min)
            
        # Prices are falling hold your buying.
        if price < min:
            min = price
            if block is not None:
                # I maintained a block and now min is updated, lets finish the block.
                # Remove stale min block.
                block.updateEnd(max)
                Blocks.append(block)
                block = None

        # One spike complete.
        if price < max and block is not None:
            block.updateEnd(max)
            Blocks.append(block)
            block = None

        # A spike is starting.
        if price > min and block is None:
           block = Block(start=min)
           # Ensure stale max spike is not considered.
           max = price

    else:
        # Ended on a high .
        if block is not None:
            block.updateEnd(max)
            Blocks.append(block)

    # All the blocks are considered, lets find max.
    maxMargin = 0
    maxBlock = None
    for block in Blocks:
        if block.margin() > maxMargin:
            maxMargin = block.margin()
            maxBlock = block

    # Couldn't find a good trade.
    if maxBlock is not None:
        print ("Max Margin {}, BUY {}, SELL {}".format(maxBlock.margin(), maxBlock.start, maxBlock.end))
    else:
        print ("Margin 0")

vals = [1,2,3]
GetMaxProfit(vals)

for block in Blocks:
    print("Margin {}, BUY {}, SELL {}".format(block.margin(), block.start, block.end))
