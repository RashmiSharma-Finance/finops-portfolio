# EXERCISE 1 - Day 1: AWS Cost Architecture
**Phase 1, Week 1** | **Duration: 1-2 hours** | **Difficulty: Easy**

---

## Today's Goal
Complete your AWS account setup, understand AWS cost model basics, and export your first cost data.

---

## THEORY (30 minutes)

### Step 1: Read AWS Pricing Fundamentals
- **Time**: 15 minutes  
- **Resource**: AWS Official Docs

**Key concepts to understand**:
1. **On-Demand Pricing** - Pay per hour/second (most expensive)
2. **Reserved Instances** - Pay upfront for discount (cheaper)
3. **Savings Plans** - Flexible discount on compute (AWS/EC2)
4. **Spot Instances** - Spare capacity at huge discount (cheapest but interruptible)

**Questions to answer** (write in `learning_log.md`):
- What's the difference between On-Demand and Reserved Instances?
- Why is Spot cheaper?
- How do you estimate monthly cost?

---

### Step 2: Watch Video (15 minutes)
Watch this AWS video: **"Getting Started with AWS Cost Explorer"**
- Link: https://www.youtube.com/watch?v=8r8AYKnCt2w (AWS official)
- Or search: "AWS Cost Explorer Tutorial" on YouTube
- Key sections: 0:00-15:00 (first 15 min is enough for today)

**What to pay attention to**:
- How Cost Explorer interface works
- Cost breakdown by service
- Time period filtering
- Exporting cost data

---

## PRACTICE (60 minutes)

### Task 1: Create AWS Account (if not already done)
**Time: 5 minutes**

- [ ] Go to https://aws.amazon.com
- [ ] Click "Create AWS Account"
- [ ] Enter email, password, account name
- [ ] Enter payment method (credit card)
- [ ] Verify email & phone
- [ ] Choose support plan (Free tier is fine for now)

**Note**: You get $300 free credits if you're new!

---

### Task 2: Enable Cost & Usage Report (CUR)
**Time: 10 minutes**

This is where AWS stores detailed cost data you'll analyze.

**Steps**:

1. **Login to AWS Console**
   - Go to https://console.aws.amazon.com
   - Use your AWS account email

2. **Navigate to Billing**
   - Search for "Billing" in search bar (top of console)
   - Click "Billing and Cost Management"

3. **Enable Cost & Usage Reports**
- Left sidebar - Cost & Usage Reports
   - Click "Create report"
   - Fill in:
     - Report name: `monthly-cost-report`
     - Include resource IDs: Yes
     - Time granularity: Monthly
     - Report versioning: Overwrite
   - Click "Next"

4. **Configure S3 Bucket**
   - Click "Configure"
   - Click "Create bucket"
   - Bucket name: `your-name-aws-costs-2026` (make unique)
   - Region: us-east-1
   - Click "Create bucket"
   - Check "I have confirmed..." checkbox
   - Click "Next"
   - Review and **Create report**

**DONE!** CUR will generate tomorrow (usually takes 24 hours)

---

### Task 3: Explore Cost Explorer (Right Now!)
**Time: 10 minutes**

1. **In AWS Console**, go to **Billing & Cost Management**
2. **Left sidebar** - **Cost Explorer**
3. You'll see your current costs (probably $0 if brand new)

**Explore these views**:
- [ ] **By Service**: Which services cost the most?
- [ ] **By Region**: Which region costs most?
- [ ] **By Time**: Cost trend over time
- [ ] **By Tag**: If you have tags, breakdown by tag

**Screenshot**: Take a screenshot of Cost Explorer for your `learning_log.md`

---

### Task 4: Create Learning Log
**Time: 5 minutes**

Create a file in your repo: `phase1_learning_log.md`

```markdown
# Phase 1 - Learning Log

## Exercise 1 - Day 1: AWS Cost Architecture

### Date: June 7, 2026
### Time spent: X hours

### Theory Learned
- On-Demand vs Reserved vs Spot instances
- [What else?]

### Practice Completed
- DONE: AWS account created
- DONE: CUR enabled
- DONE: Cost Explorer explored

### Key Insight
[One sentence summary of what you learned]

### Questions I have
[Anything unclear?]

### Blocker
[If stuck, write here]

---
```

**Document your learning as you go!** This is important.

---

### Task 5: Write Your First Reflection (10 minutes)
**Time: 10 minutes**

In your `phase1_learning_log.md`, write:

**Section: "Cost Model Mindmap"**

```
AWS Pricing Model
├── On-Demand
│   ├── Definition: Pay per hour/second
│   ├── Cost: Highest
│   └── Use case: [Your answer]
├── Reserved Instances
│   ├── Definition: Pay upfront
│   ├── Discount: 30-70%
│   └── Use case: [Your answer]
├── Savings Plans
│   ├── Definition: [Your answer]
│   ├── Discount: [Your answer]
│   └── Use case: [Your answer]
└── Spot Instances
    ├── Definition: [Your answer]
    ├── Discount: 50-90%

```

Fill in the blanks!

---

### Task 6: Prepare for Day 2
**Time: 5 minutes**

- [ ] Bookmark AWS Cost Explorer
- [ ] Note your S3 bucket name (you'll need it tomorrow)
- [ ] Bookmark this learning log

---

## 📝 What to Commit to GitHub Today

```bash
# In your terminal:
cd /Users/rashmisharma/Documents/Finance\ 2026/demo-repository

# Create phase1 directory
mkdir -p phase1/exercises
cd phase1

# Create learning log
touch exercises/learning_log.md

# Add your notes to learning_log.md
# Then commit:
git add .
git commit -m "Exercise 1: Day 1 - AWS Cost Architecture basics"
git push
```

---

## Completion Checklist

- [ ] Read AWS pricing fundamentals
- [ ] Watched AWS Cost Explorer video
- [ ] Created AWS account
- [ ] Enabled CUR (will generate tomorrow)
- [ ] Explored Cost Explorer interface
- [ ] Created `phase1_learning_log.md`
- [ ] Filled in cost model mindmap
- [ ] Committed to GitHub

---

## Success Criteria

By end of today, you should:
DONE: Understand basic AWS pricing model  
DONE: Have AWS account with CUR enabled  
DONE: Have explored Cost Explorer  
DONE: Started documenting your learning  

---

## 📅 Tomorrow's Exercise (Day 2)

**Topic**: Cost & Usage Report (CUR) Deep Dive
- Parse your first CUR file
- Understand line items
- Extract basic cost metrics
- Your first Python script

---

## Troubleshooting

**"I don't have AWS account"**
→ Create free account here: https://aws.amazon.com/free/

**"Where's Cost Explorer?"**
→ Billing & Cost Management dashboard → Left sidebar → Cost Explorer

**"CUR not showing data yet?"**
→ Normal - CUR takes 24 hours to generate. Continue to Day 2.

**"I'm confused about Reserved Instances vs Spot"**
→ Don't worry! You'll understand deeply by Exercise 5. For now:
- Reserved = predictable, cheaper
- Spot = unpredictable, cheapest

---

## Resources

- AWS Pricing: https://aws.amazon.com/pricing/
- Cost Explorer Guide: https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html
- CUR Documentation: https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html

---

## ✍️ Now: Write in Your Learning Log

**Time**: 2 minutes

Open `phase1_learning_log.md` and write:

```
## Exercise 1 - Day 1 Completed

### What I learned
[3-4 sentences about AWS cost architecture]

### What surprised me
[One thing you didn't expect]

### Tomorrow I will
[What you'll do in Exercise 1 Day 2]
```

---

**Status**: IN PROGRESS  
**Next Step**: Complete tasks 1-6 above  
**Time Estimate**: 1-2 hours

You've got this!

---

*Ready? Start with Task 1 now!*
