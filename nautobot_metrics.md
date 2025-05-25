# Nautobot Metrics & Dashboards Guide

## Introduction

This document provides a comprehensive guide to defining, collecting, and visualizing metrics for the Nautobot platform. Its purpose is to establish a standardized framework for understanding Nautobot's value, usage, performance, and impact through key performance indicators (KPIs) and conceptual dashboard designs. By leveraging the metrics and dashboard ideas presented here, organizations can gain deeper insights into their Nautobot deployment, optimize its usage, and effectively communicate its benefits.

## Table of Contents

1.  [Nautobot Core Metric Categories](#nautobot-core-metric-categories)
    *   [1.1 Return on Investment (ROI) Metrics](#11-return-on-investment-roi-metrics)
    *   [1.2 User Activity Telemetry](#12-user-activity-telemetry)
    *   [1.3 Plugin & Integration Activity Metrics](#13-plugin--integration-activity-metrics)
    *   [1.4 System Performance Metrics](#14-system-performance-metrics)
    *   [1.5 Business Impact Metrics](#15-business-impact-metrics)
2.  [Specific ROI Metrics](#specific-roi-metrics)
    *   [2.1 Efficiency Gains from Automation (User Activity & Application Execution)](#21-efficiency-gains-from-automation-user-activity--application-execution)
    *   [2.2 Cost Savings](#22-cost-savings)
    *   [2.3 Value Provided by Automation Tools](#23-value-provided-by-automation-tools-eg-ansible-gitlab-cicd-integrated-with-nautobot)
    *   [2.4 Business Impact (Direct & Indirect)](#24-business-impact-direct--indirect)
3.  [User Activity Telemetry Metrics](#user-activity-telemetry-metrics)
    *   [3.1 User Authentication & Session Management](#31-user-authentication--session-management)
    *   [3.2 CRUD Operations (Create, Read, Update, Delete)](#32-crud-operations-create-read-update-delete)
    *   [3.3 Feature Usage](#33-feature-usage)
    *   [3.4 User Engagement & Workflow](#34-user-engagement--workflow)
4.  [Plugin & Integration Activity Metrics](#plugin--integration-activity-metrics)
    *   [4.1 Golden Configuration Plugin Metrics](#41-golden-configuration-plugin-metrics)
    *   [4.2 SSoT Plugin Metrics](#42-ssot-plugin-metrics)
    *   [4.3 Device Lifecycle Management (DLM) Plugin Metrics](#43-device-lifecycle-management-dlm-plugin-metrics)
    *   [4.4 General Plugin & Job Metrics](#44-general-plugin--job-metrics)
5.  [Metric Naming Conventions and Groupings](#metric-naming-conventions-and-groupings)
    *   [5.1 Naming Convention](#51-naming-convention)
    *   [5.2 Metric Groupings for Dashboards & Reporting](#52-metric-groupings-for-dashboards--reporting)
6.  [Conceptual Dashboard Designs (Suite of 20)](#conceptual-dashboard-designs-suite-of-20)
    *   [6.1 Executive ROI & Business Value Dashboard](#61-executive-roi--business-value-dashboard)
    *   [6.2 Automation Program Health Dashboard](#62-automation-program-health-dashboard)
    *   [6.3 Risk & Compliance Overview Dashboard](#63-risk--compliance-overview-dashboard)
    *   [6.4 Nautobot Platform Health & Usage Dashboard](#64-nautobot-platform-health--usage-dashboard)
    *   [6.5 User Activity & Engagement Dashboard](#65-user-activity--engagement-dashboard)
    *   [6.6 Golden Configuration - Compliance Deep Dive](#66-golden-configuration---compliance-deep-dive)
    *   [6.7 Golden Configuration - Operational Dashboard](#67-golden-configuration---operational-dashboard)
    *   [6.8 SSoT - Data Reconciliation & Integrity Dashboard](#68-ssot---data-reconciliation--integrity-dashboard)
    *   [6.9 SSoT - Impact Analysis Dashboard](#69-ssot---impact-analysis-dashboard)
    *   [6.10 Device Lifecycle Management (DLM) - Efficiency Dashboard](#610-device-lifecycle-management-dlm---efficiency-dashboard)
    *   [6.11 DLM - Operational Status Dashboard](#611-dlm---operational-status-dashboard)
    *   [6.12 Job Execution & Automation Performance Dashboard](#612-job-execution--automation-performance-dashboard)
    *   [6.13 Ansible Automation (via Nautobot) Performance](#613-ansible-automation-via-nautobot-performance)
    *   [6.14 CI/CD Pipeline Integration Dashboard](#614-cicd-pipeline-integration-dashboard)
    *   [6.15 Network Services Health (derived from Nautobot data)](#615-network-services-health-derived-from-nautobot-data)
    *   [6.16 "Time to Value" Dashboard](#616-time-to-value-dashboard)
    *   [6.17 "Error Reduction & Quality Improvement" Dashboard](#617-error-reduction--quality-improvement-dashboard)
    *   [6.18 Plugin Ecosystem Overview Dashboard](#618-plugin-ecosystem-overview-dashboard)
    *   [6.19 "What-If" Scenario Planning Dashboard (Conceptual)](#619-what-if-scenario-planning-dashboard-conceptual)
    *   [6.20 Security & Audit Log Activity Dashboard](#620-security--audit-log-activity-dashboard)
7.  [High-Level Dashboard Implementation Guides](#high-level-dashboard-implementation-guides)
    *   [7.1 Executive ROI & Business Value Dashboard](#71-executive-roi--business-value-dashboard)
    *   [7.2 Automation Program Health Dashboard](#72-automation-program-health-dashboard)
    *   [7.3 Risk & Compliance Overview Dashboard](#73-risk--compliance-overview-dashboard)
    *   [7.4 Nautobot Platform Health & Usage Dashboard](#74-nautobot-platform-health--usage-dashboard)
    *   [7.5 User Activity & Engagement Dashboard](#75-user-activity--engagement-dashboard)
    *   [7.6 Golden Configuration - Compliance Deep Dive](#76-golden-configuration---compliance-deep-dive)
    *   [7.7 Golden Configuration - Operational Dashboard](#77-golden-configuration---operational-dashboard)
    *   [7.8 SSoT - Data Reconciliation & Integrity Dashboard](#78-ssot---data-reconciliation--integrity-dashboard)
    *   [7.9 SSoT - Impact Analysis Dashboard](#79-ssot---impact-analysis-dashboard)
    *   [7.10 Device Lifecycle Management (DLM) - Efficiency Dashboard](#710-device-lifecycle-management-dlm---efficiency-dashboard)
    *   [7.11 DLM - Operational Status Dashboard](#711-dlm---operational-status-dashboard)
    *   [7.12 Job Execution & Automation Performance Dashboard](#712-job-execution--automation-performance-dashboard)
    *   [7.13 Ansible Automation (via Nautobot) Performance](#713-ansible-automation-via-nautobot-performance)
    *   [7.14 CI/CD Pipeline Integration Dashboard](#714-cicd-pipeline-integration-dashboard)
    *   [7.15 Network Services Health (derived from Nautobot data)](#715-network-services-health-derived-from-nautobot-data)
    *   [7.16 "Time to Value" Dashboard](#716-time-to-value-dashboard)
    *   [7.17 "Error Reduction & Quality Improvement" Dashboard](#717-error-reduction--quality-improvement-dashboard)
    *   [7.18 Plugin Ecosystem Overview Dashboard](#718-plugin-ecosystem-overview-dashboard)
    *   [7.19 "What-If" Scenario Planning Dashboard (Conceptual)](#719-what-if-scenario-planning-dashboard-conceptual)
    *   [7.20 Security & Audit Log Activity Dashboard](#720-security--audit-log-activity-dashboard)
8.  [Conclusion](#conclusion)

---

# Nautobot Core Metric Categories

This document defines and describes the core metric categories for the Nautobot project. These categories provide a framework for understanding the value, usage, performance, and impact of Nautobot.

## 1.1 Return on Investment (ROI) Metrics

**Purpose:** To quantify the financial and operational value derived from implementing and utilizing Nautobot. This category focuses on the efficiencies gained through automation, time saved, and cost reductions.

**Insights:**
*   **Cost Savings:**
    *   Reduction in manual labor hours for network operations tasks (e.g., device provisioning, configuration backups, compliance checks).
    *   Decreased mean time to resolution (MTTR) for network incidents due to improved data accuracy and automation capabilities.
    *   Avoidance of costs associated with network outages or misconfigurations prevented by Nautobot's data integrity and automation features.
*   **Efficiency Gains:**
    *   Time saved in network design and planning processes.
    *   Increased speed of service delivery (e.g., provisioning new VLANs, deploying new devices).
    *   Improved operational efficiency by reducing repetitive manual tasks.
*   **Value of Automation:**
    *   Quantifiable benefits of specific automation use cases built on Nautobot (e.g., automated device onboarding, automated OS upgrades).
    *   Number of automated tasks executed successfully.
    *   Reduction in errors previously caused by manual intervention.

## 1.2 User Activity Telemetry

**Purpose:** To understand how users interact with the Nautobot system, identify popular features, and pinpoint areas where usability could be improved. This data helps in prioritizing feature development and user training efforts.

**Insights:**
*   **User Engagement:**
    *   Number of active users (daily, weekly, monthly).
    *   Session duration and frequency of logins.
    *   Most frequently accessed pages and features.
    *   Adoption rate of new features.
*   **Workflow Patterns:**
    *   Common sequences of actions performed by users.
    *   Usage of specific UI elements (e.g., buttons, forms, filters).
    *   Identification of potential bottlenecks or pain points in user workflows.
*   **API Usage:**
    *   Volume of API requests (overall and per endpoint).
    *   Most frequently used API endpoints.
    *   Identification of users or services leveraging the API.
    *   Error rates for API requests.
*   **Data Interaction:**
    *   Frequency of create, read, update, delete (CRUD) operations on different data models (e.g., devices, IPs, VLANs).
    *   Popularity of specific data objects.
    *   Usage of search and filtering capabilities.

## 1.3 Plugin & Integration Activity Metrics

**Purpose:** To measure the usage, performance, and effectiveness of Nautobot plugins and integrations. This helps in understanding the value specific plugins provide and identifying areas for improvement or further development.

**Insights:**
*   **Golden Configuration Plugin:**
    *   Number of devices actively managed by the Golden Configuration plugin.
    *   Frequency of configuration compliance checks.
    *   Rate of compliance drift (number of non-compliant devices over time).
    *   Time saved by automating configuration backups and remediation.
    *   Number of automated configuration remediation actions taken.
*   **Single Source of Truth (SSoT) Plugin:**
    *   Number of external systems integrated via SSoT.
    *   Volume of data synchronized between Nautobot and external systems.
    *   Frequency of SSoT job executions.
    *   Error rates for SSoT jobs.
    *   Data consistency improvements resulting from SSoT (e.g., reduction in discrepancies).
*   **Device Lifecycle Management (DLM) Plugin:**
    *   Number of devices managed through different lifecycle stages (e.g., planned, provisioned, active, retired).
    *   Time taken to transition devices through lifecycle stages.
    *   Adherence to defined lifecycle policies.
    *   Reduction in manual effort for device onboarding and decommissioning.
*   **General Plugin Usage:**
    *   Adoption rate of different installed plugins.
    *   User interaction with plugin-specific features.
    *   Performance impact of plugins on the overall system.

## 1.4 System Performance Metrics

**Purpose:** To monitor the health, stability, and responsiveness of the Nautobot application and its underlying infrastructure. These metrics are crucial for ensuring a good user experience, identifying performance bottlenecks, and planning capacity.

**Insights:**
*   **Application Performance:**
    *   Average and peak response times for web UI pages and API endpoints.
    *   Application error rates (e.g., HTTP 5xx errors).
    *   Request throughput (requests per second/minute).
    *   Celery worker performance (e.g., task queue length, task execution time).
*   **Resource Utilization:**
    *   CPU, memory, and disk I/O utilization of Nautobot servers.
    *   Database performance (e.g., query latency, connection pooling).
    *   Network bandwidth consumption.
*   **Uptime and Availability:**
    *   System uptime percentage.
    *   Mean time between failures (MTBF).
    *   Availability of critical system components (e.g., web servers, database, Redis).
*   **Scalability:**
    *   Performance under load (e.g., during peak usage or large data imports).
    *   Identification of scaling limits and bottlenecks.

## 1.5 Business Impact Metrics

**Purpose:** To assess the broader effects of Nautobot on business operations and strategic objectives. These metrics often overlap with ROI but can also include qualitative aspects and lagging indicators that demonstrate long-term value.

**Insights:**
*   **Strategic Alignment:**
    *   Contribution of Nautobot to achieving specific business goals (e.g., digital transformation, infrastructure modernization).
    *   Improvement in agility and responsiveness to business needs.
    *   Enablement of new business capabilities or services.
*   **Risk Reduction:**
    *   Reduction in security vulnerabilities through consistent configuration and compliance.
    *   Improved auditability and compliance posture.
    *   Decrease in human error-related incidents.
*   **Operational Excellence:**
    *   Enhancements in standardization of network configurations and processes.
    *   Improved collaboration between network, security, and application teams.
    *   Long-term trends in operational efficiency and cost reduction.
*   **User & Stakeholder Satisfaction:**
    *   Qualitative feedback from users and stakeholders on Nautobot's effectiveness.
    *   Impact on employee morale and job satisfaction for network teams (e.g., by reducing tedious manual work).
    *   Perceived value of Nautobot in supporting business objectives.

---

# Specific ROI Metrics

This section details specific metrics for quantifying the Return on Investment (ROI) from Nautobot, categorized by focus areas. Each metric includes its description, calculation formula, data sources, pros, cons, and a business context example.

## 2.1 Efficiency Gains from Automation (User Activity & Application Execution)

### a. Time Saved per Automated Task
*   **Metric Name:** Time Saved per Automated Task
*   **Description:** Measures the reduction in time required to complete a specific task due to automation with Nautobot.
*   **Calculation Formula:** `Time_Manual - Time_Automated` (typically measured in hours)
*   **Data Sources:** Manual time tracking (before automation), Nautobot job logs (for automated task duration), user/team estimations.
*   **Pros:** Directly quantifies time savings, easy to understand and communicate.
*   **Cons:** Requires accurate baseline data for manual task duration, automated task time might vary.
*   **Business Context Example:** Provisioning a new VLAN manually took 2 hours. With a Nautobot automation, it now takes 15 minutes. Time saved per task = 1.75 hours.

### b. Reduction in Manual Error Rates
*   **Metric Name:** Reduction in Manual Error Rates
*   **Description:** Measures the decrease in errors for tasks that were previously manual and are now automated.
*   **Calculation Formula:** `(Error_Rate_Manual - Error_Rate_Automated) / Error_Rate_Manual * 100%`
*   **Data Sources:** Incident logs, change management records, manual error tracking spreadsheets (historical), Nautobot automation success/failure logs.
*   **Pros:** Highlights improvements in quality and reliability, can be linked to cost savings from error avoidance.
*   **Cons:** Requires consistent error tracking mechanisms both before and after automation, attributing errors solely to manual vs. automated processes can be complex.
*   **Business Context Example:** Manual device configuration changes had a 10% error rate leading to rollbacks. Post-automation with Nautobot, the error rate for the same changes dropped to 1%. Reduction = 90%.

### c. Increased Task Throughput
*   **Metric Name:** Increased Task Throughput
*   **Description:** Measures the number of tasks (e.g., device configurations, compliance checks) completed in a specific period with automation compared to manual methods.
*   **Calculation Formula:** `(Tasks_Completed_Automated - Tasks_Completed_Manual) / Tasks_Completed_Manual * 100%` (for a given time period) OR `Number_of_Tasks_Automated / Time_Period`
*   **Data Sources:** Nautobot job logs, change management systems, operational dashboards.
*   **Pros:** Demonstrates increased operational capacity, easy to visualize performance improvements.
*   **Cons:** Doesn't account for the complexity of tasks, higher throughput doesn't always mean higher value if tasks are trivial.
*   **Business Context Example:** Previously, the team could deploy 20 firewall policy updates per week. With Nautobot automation, they can now deploy 100, showing a 400% increase in throughput.

### d. Automation Adoption Rate
*   **Metric Name:** Automation Adoption Rate
*   **Description:** Measures the percentage of target tasks or processes that are now being executed via Nautobot automation instead of manually.
*   **Calculation Formula:** `(Number_of_Tasks_Automated / Total_Potential_Tasks_for_Automation) * 100%` OR `(Number_of_Users_Using_Automation / Total_Target_Users) * 100%`
*   **Data Sources:** Nautobot usage logs, user surveys, team leader reports, predefined list of automatable tasks.
*   **Pros:** Indicates user acceptance and integration of automation into daily workflows, reflects cultural shift.
*   **Cons:** Identifying "Total Potential Tasks" can be subjective, users might use automation but not for all intended tasks.
*   **Business Context Example:** Out of 50 identified repetitive network tasks, 30 are now automated via Nautobot, resulting in an Automation Adoption Rate of 60%.

## 2.2 Cost Savings

### a. Reduced Operational Costs
*   **Metric Name:** Reduced Operational Costs
*   **Description:** Measures the reduction in operational expenditures due to Nautobot automation, such as reduced labor for manual tasks or fewer incidents requiring costly remediation.
*   **Calculation Formula:** `(Manual_Labor_Cost_Before - Manual_Labor_Cost_After) + (Incident_Cost_Before - Incident_Cost_After)`
*   **Data Sources:** Financial records, HR data (average salaries), incident management system, project budget reports.
*   **Pros:** Directly translates to bottom-line savings, strong justification for investment.
*   **Cons:** Requires accurate cost allocation, attributing savings solely to Nautobot can be challenging if other factors are at play.
*   **Business Context Example:** By automating device patching, the company reduced overtime pay for engineers by $10,000 annually and decreased incident-related costs by $20,000. Total Reduced Operational Costs = $30,000.

### b. Cost Avoidance
*   **Metric Name:** Cost Avoidance
*   **Description:** Quantifies the costs avoided by using Nautobot, such as preventing outages, compliance penalties, or security breaches.
*   **Calculation Formula:** `Sum_of_Potential_Costs_Avoided` (e.g., `Potential_Outage_Cost * Likelihood_Reduction_Due_To_Automation`)
*   **Data Sources:** Industry reports on outage/breach costs, internal risk assessments, compliance penalty schedules, Nautobot logs showing preventative actions (e.g., compliance remediation).
*   **Pros:** Highlights proactive value and risk mitigation, can be very significant figures.
*   **Cons:** Based on estimations and probabilities, can be perceived as less concrete than direct cost savings. Requires robust risk assessment.
*   **Business Context Example:** A potential network outage, estimated to cost $500,000, was prevented by a Nautobot-driven automated compliance check that identified and remediated a critical misconfiguration. Cost Avoidance = $500,000.

### c. Reduced Tooling Costs
*   **Metric Name:** Reduced Tooling Costs
*   **Description:** Measures the savings achieved by replacing or consolidating existing commercial software/tools with Nautobot and its ecosystem (including open-source integrations).
*   **Calculation Formula:** `Sum_of_License_Fees_of_Replaced_Tools - Cost_of_Nautobot_Implementation_and_Maintenance` (if applicable, or just `Sum_of_License_Fees` if Nautobot is already in place)
*   **Data Sources:** Software procurement records, vendor invoices, IT budget.
*   **Pros:** Clear and tangible savings, simplifies the IT landscape.
*   **Cons:** May not apply if Nautobot augments rather than replaces tools, requires accounting for potential migration/integration costs.
*   **Business Context Example:** The company decommissioned a commercial IPAM solution with an annual license fee of $25,000 after migrating its functionalities to Nautobot. Reduced Tooling Costs = $25,000 annually.

### d. Cost of Inaction
*   **Metric Name:** Cost of Inaction
*   **Description:** Estimates the opportunity cost or continued expenses incurred by *not* implementing or expanding Nautobot automation for specific processes.
*   **Calculation Formula:** `(Current_Manual_Process_Cost + Current_Error_Related_Costs + Missed_Opportunity_Costs) - Projected_Nautobot_Automation_Cost` (calculated annually or per project)
*   **Data Sources:** Existing operational cost data, error logs, business strategy documents, market analysis for missed opportunities.
*   **Pros:** Compelling argument for adopting automation by highlighting ongoing negative financial impact.
*   **Cons:** Can be complex to calculate accurately, especially "missed opportunity costs"; may be perceived as theoretical.
*   **Business Context Example:** Continuing with manual firewall rule management costs $80k/year in labor and $20k/year in error remediation. Automating with Nautobot is projected to cost $30k/year (including development and maintenance). The Cost of Inaction is $70k/year ($100k - $30k).

## 2.3 Value Provided by Automation Tools (e.g., Ansible, GitLab CI/CD integrated with Nautobot)

This section focuses on metrics that demonstrate the value derived from integrating Nautobot as a Single Source of Truth (SSoT) with other automation tools.

### a. Deployment Frequency
*   **Metric Name:** Deployment Frequency
*   **Description:** Measures how often changes (e.g., configurations, software updates) are deployed to production or pre-production environments, enabled by reliable data from Nautobot.
*   **Calculation Formula:** `Number_of_Deployments / Time_Period` (e.g., deployments per week, per month)
*   **Data Sources:** CI/CD pipeline logs (GitLab CI, Jenkins), change management records, deployment scripts.
*   **Pros:** Indicates agility and speed of delivering changes, reflects confidence in the deployment process.
*   **Cons:** High frequency doesn't inherently mean high quality; deployments could be small, insignificant changes.
*   **Business Context Example:** After integrating Ansible with Nautobot for configuration data, the network team increased their deployment frequency for standard switch port configurations from monthly to weekly, enabling faster service delivery.

### b. Change Failure Rate (CFR)
*   **Metric Name:** Change Failure Rate
*   **Description:** Measures the percentage of deployments or changes that result in a failure, incident, or require remediation, with Nautobot data used for pre-validation.
*   **Calculation Formula:** `(Number_of_Failed_Changes / Total_Number_of_Changes) * 100%`
*   **Data Sources:** Incident management system, change management records, CI/CD pipeline logs, monitoring tools.
*   **Pros:** Directly measures the quality and reliability of changes, lower CFR indicates better pre-validation and testing.
*   **Cons:** Defining "failure" can be subjective, not all failures have the same impact.
*   **Business Context Example:** By using Nautobot data to pre-validate Ansible playbooks, the Change Failure Rate for router OS upgrades dropped from 15% to 3%, reducing service disruptions.

### c. Mean Time to Recovery (MTTR)
*   **Metric Name:** Mean Time to Recovery (MTTR)
*   **Description:** Measures the average time taken to restore service after a failure, where Nautobot's accurate data and automation capabilities facilitate faster rollbacks or reprovisioning.
*   **Calculation Formula:** `Total_Downtime_Duration_from_Incidents / Number_of_Incidents`
*   **Data Sources:** Incident management system, monitoring alerts, Nautobot logs (if involved in automated recovery).
*   **Pros:** Critical indicator of operational stability and resilience, directly impacts user experience and business continuity.
*   **Cons:** Can be skewed by a few very long or very short incidents, requires accurate incident timing.
*   **Business Context Example:** When a misconfiguration occurred, the team was able to use Nautobot's data and an automated rollback script to restore services in 30 minutes, compared to a previous manual MTTR of 4 hours.

### d. Reduction in Pre-Deployment Validation Time
*   **Metric Name:** Reduction in Pre-Deployment Validation Time
*   **Description:** Measures the time saved in the pre-deployment phase by leveraging Nautobot as the SSoT for configuration data, eliminating manual data gathering and cross-referencing.
*   **Calculation Formula:** `Manual_Validation_Time_Before_Nautobot - Automated_Validation_Time_With_Nautobot`
*   **Data Sources:** Change management records, team surveys, CI/CD logs (if validation steps are logged).
*   **Pros:** Frees up engineering time, speeds up the overall change lifecycle.
*   **Cons:** Requires estimation of manual validation time, benefits might be less visible if previous validation was informal.
*   **Business Context Example:** Manually validating parameters for a new site deployment used to take network engineers 8 hours. By pulling validated data directly from Nautobot via Ansible, pre-deployment validation now takes 1 hour. Time saved = 7 hours per deployment.

## 2.4 Business Impact (Direct & Indirect)

### a. Improved Service Delivery Time
*   **Metric Name:** Improved Service Delivery Time
*   **Description:** Measures the reduction in time taken to deliver new services or make changes requested by the business or customers, thanks to Nautobot-enabled automation.
*   **Calculation Formula:** `Time_to_Deliver_Service_Manual - Time_to_Deliver_Service_Automated`
*   **Data Sources:** Service request tracking systems (e.g., ServiceNow, Jira), project management tools, customer feedback.
*   **Pros:** Directly impacts business agility and customer satisfaction, demonstrates responsiveness to market needs.
*   **Cons:** Can be influenced by factors outside of network automation (e.g., upstream processes), requires clear definition of "service delivery" start and end points.
*   **Business Context Example:** Provisioning a new virtual server for a development team, which involves network configuration, previously took 3 days. With Nautobot automating IP allocation, VLAN assignment, and firewall rule updates, it now takes 4 hours. Service Delivery Time improved by 2.5 days.

### b. Enhanced Compliance Posture & Reduced Audit Costs
*   **Metric Name:** Enhanced Compliance Posture & Reduced Audit Costs
*   **Description:** Measures the improvement in compliance adherence and the reduction in costs associated with audits, due to consistent configurations and automated evidence gathering via Nautobot (e.g., using Golden Config plugin).
*   **Calculation Formula:** `(Cost_of_NonCompliance_Before - Cost_of_NonCompliance_After) + (Audit_Preparation_Time_Cost_Before - Audit_Preparation_Time_Cost_After)` OR `Percentage_Improvement_in_Compliance_Checks`
*   **Data Sources:** Audit reports, compliance records, Golden Configuration plugin reports, finance department (for cost of fines/penalties), time tracking for audit preparation.
*   **Pros:** Reduces risk of fines and reputational damage, demonstrates control and governance, saves time and resources.
*   **Cons:** Quantifying "cost of non-compliance" can be difficult unless actual fines were levied, benefits are sometimes preventative and thus harder to measure directly.
*   **Business Context Example:** The company reduced audit preparation time by 80 hours per audit and avoided potential fines of $100,000 by using Nautobot's Golden Configuration plugin to maintain and prove device compliance, leading to a total saving/avoidance of $100,000 + (80 hours * avg_hourly_rate).

### c. Increased Innovation Capacity
*   **Metric Name:** Increased Innovation Capacity
*   **Description:** Measures the extent to which engineering teams are freed from operational toil, allowing them to focus on innovation, new projects, and strategic initiatives.
*   **Calculation Formula:** `(Time_Spent_on_Toil_Before_Nautobot - Time_Spent_on_Toil_After_Nautobot) / Total_Engineering_Time * 100%` OR `Number_of_New_Projects_or_Innovations_Enabled`
*   **Data Sources:** Time tracking systems, project management tools, engineering team surveys/feedback, resource allocation reports.
*   **Pros:** Links automation directly to strategic business value, improves employee morale and skill development.
*   **Cons:** "Innovation" can be hard to quantify directly, requires honest time tracking and allocation.
*   **Business Context Example:** By automating 60% of their routine network tasks with Nautobot, the network engineering team was able to reallocate 500 hours per quarter from operational toil to developing a new network analytics platform, accelerating its launch.

### d. Reduced Mean Time To Resolution (MTTR) for Incidents
*   **Metric Name:** Reduced Mean Time To Resolution (MTTR) for Incidents
*   **Description:** Measures the average time taken to resolve network incidents, highlighting the impact of Nautobot's accurate data and automation in diagnostics and remediation. (Note: This is related to the MTTR in section 3.c but focused on broader incident resolution, not just change failures).
*   **Calculation Formula:** `Average_Incident_Resolution_Time_Before_Nautobot - Average_Incident_Resolution_Time_After_Nautobot`
*   **Data Sources:** Incident management system (e.g., PagerDuty, ServiceNow), monitoring tools, Nautobot logs (if used in diagnostics/remediation).
*   **Pros:** Directly impacts business continuity and user productivity, tangible operational improvement.
*   **Cons:** Requires consistent incident logging and categorization, attributing improvements solely to Nautobot can be difficult if other operational changes occur.
*   **Business Context Example:** Previously, network troubleshooting often involved manually checking multiple data sources, leading to an average MTTR of 2 hours. With Nautobot providing a centralized SSoT and enabling automated diagnostics scripts, MTTR was reduced to 45 minutes.

---

# User Activity Telemetry Metrics

This section defines specific metrics to track user interactions within Nautobot, providing insights into how the platform is used. For each metric, details on its description, data sources, potential insights, and suggested grouping/type are provided.

## 3.1 User Authentication & Session Management

### a. Successful Logins
*   **Metric Name:** `nautobot.user_activity.authentication.login.success.count`
*   **Description:** Counts the number of successful user login attempts.
*   **Data Source Ideas:** Nautobot application logs (specifically authentication logs), web server access logs (filtered for login endpoints).
*   **Potential Insights:** Overall system usage, peak login times, user adoption trends. Can indicate the active user base.
*   **Suggested Grouping/Type:** Authentication; Counter

### b. Failed Login Attempts
*   **Metric Name:** `nautobot.user_activity.authentication.login.failed.count`
*   **Description:** Counts the number of failed user login attempts.
*   **Data Source Ideas:** Nautobot application logs (authentication failure logs), security information and event management (SIEM) systems.
*   **Potential Insights:** Potential security issues (e.g., brute-force attacks), user credential problems, issues with identity providers.
*   **Suggested Grouping/Type:** Authentication, Security; Counter

### c. Active User Sessions
*   **Metric Name:** `nautobot.user_activity.session_management.active_sessions.gauge`
*   **Description:** Measures the number of currently active user sessions.
*   **Data Source Ideas:** Nautobot application's session management system (e.g., Django session store in database or cache).
*   **Potential Insights:** Real-time system load, concurrent user activity, capacity planning for server resources.
*   **Suggested Grouping/Type:** Authentication, Performance; Gauge

### d. Session Duration (Average/Max/Min)
*   **Metric Name:** `nautobot.user_activity.session_management.session_duration.seconds` (aggregations: `avg`, `max`, `min`)
*   **Description:** Measures the length of user sessions.
*   **Data Source Ideas:** Nautobot application logs (login and logout events), web server logs (by correlating session IDs).
*   **Potential Insights:** User engagement levels, how long users typically stay in the system, identification of unusually long or short sessions.
*   **Suggested Grouping/Type:** Authentication, Engagement; Timer/Distribution

### e. Logins by User/Group
*   **Metric Name:** `nautobot.user_activity.authentication.login.by_user.count`, `nautobot.user_activity.authentication.login.by_group.count`
*   **Description:** Counts successful logins, aggregated by individual user or user group.
*   **Data Source Ideas:** Nautobot application logs (linking login events to user/group IDs).
*   **Potential Insights:** Identifies most active users/groups, helps understand which teams rely on Nautobot most, can inform training needs.
*   **Suggested Grouping/Type:** Authentication, User Behavior; Counter (per user/group)

## 3.2 CRUD Operations (Create, Read, Update, Delete)

These metrics can be dimensioned by user, object type (e.g., `object_type:device`, `object_type:ipaddress`), and access method (UI vs API).

### a. Object Creation Count
*   **Metric Name:** `nautobot.user_activity.object_management.object.creation.count` (tags: `object_type`, `user`, `access_method`)
*   **Description:** Counts the number of new objects created in Nautobot.
*   **Data Source Ideas:** Nautobot change logs (audit trails), database triggers, application-level event streaming.
*   **Potential Insights:** Growth rate of the database, which object types are most frequently added, user activity patterns for data creation, adoption of API for provisioning.
*   **Suggested Grouping/Type:** Object Management, Data Population; Counter

### b. Object Read/View Count
*   **Metric Name:** `nautobot.user_activity.object_management.object.read.count` (tags: `object_type`, `user`, `access_method`)
*   **Description:** Counts the number of times objects are read or viewed.
*   **Data Source Ideas:** Nautobot application logs (access to object detail views, API GET requests), web server logs (for UI views).
*   **Potential Insights:** Popularity of different object types, which data is most frequently accessed, user research patterns, API usage for data retrieval.
*   **Suggested Grouping/Type:** Object Management, Data Consumption; Counter

### c. Object Update Count
*   **Metric Name:** `nautobot.user_activity.object_management.object.update.count` (tags: `object_type`, `user`, `access_method`)
*   **Description:** Counts the number of times existing objects are updated.
*   **Data Source Ideas:** Nautobot change logs, database triggers, application-level event streaming.
*   **Potential Insights:** Data churn rates, which object types are most dynamic, user activity patterns for data modification, use of API for configuration changes.
*   **Suggested Grouping/Type:** Object Management, Data Maintenance; Counter

### d. Object Deletion Count
*   **Metric Name:** `nautobot.user_activity.object_management.object.deletion.count` (tags: `object_type`, `user`, `access_method`)
*   **Description:** Counts the number of objects deleted from Nautobot.
*   **Data Source Ideas:** Nautobot change logs, database triggers, application-level event streaming.
*   **Potential Insights:** Data lifecycle management, identification of cleanup activities, user patterns for data removal, API usage for de-provisioning.
*   **Suggested Grouping/Type:** Object Management, Data Deprovisioning; Counter

## 3.3 Feature Usage

### a. Feature/Page View Frequency
*   **Metric Name:** `nautobot.user_activity.feature_usage.page_view.frequency.count` (tags: `page_url` or `feature_name`, `user`)
*   **Description:** Counts the number of views for specific features or pages (e.g., topology maps, specific plugin pages, REST API docs).
*   **Data Source Ideas:** Web server access logs, Nautobot application logs (if page views are instrumented), frontend analytics (if used).
*   **Potential Insights:** Popularity of different features/pages, identify underutilized features, understand user navigation patterns, inform UI/UX improvements.
*   **Suggested Grouping/Type:** Feature Adoption, User Behavior; Counter

### b. Job Execution Count
*   **Metric Name:** `nautobot.user_activity.feature_usage.job_execution.user_initiated.count` (tags: `job_name`, `user`, `status`)
*   **Description:** Counts the number of jobs initiated by users (as opposed to system-scheduled jobs).
*   **Data Source Ideas:** Nautobot job result logs/database, Celery logs (if jobs are processed via Celery and tagged with user info).
*   **Potential Insights:** Usage of automation features, which jobs are most popular among users, success/failure rates of user-initiated jobs, user reliance on specific automations.
*   **Suggested Grouping/Type:** Feature Adoption, Automation; Counter

### c. Filter Usage Frequency
*   **Metric Name:** `nautobot.user_activity.feature_usage.filter_usage.frequency.count` (tags: `object_type`, `filter_field`, `user`)
*   **Description:** Counts how often specific filters are applied on list views or in API queries.
*   **Data Source Ideas:** Nautobot application logs (if filter usage is logged), web server logs (by parsing query parameters).
*   **Potential Insights:** Understand common user search criteria, identify important data attributes for users, optimize database queries for frequent filters, improve UI filter options.
*   **Suggested Grouping/Type:** Feature Adoption, User Behavior; Counter

### d. Export Frequency
*   **Metric Name:** `nautobot.user_activity.feature_usage.data_export.frequency.count` (tags: `object_type`, `export_format`, `user`)
*   **Description:** Counts the number of times data is exported from Nautobot (e.g., CSV, JSON).
*   **Data Source Ideas:** Nautobot application logs (if exports are logged), web server logs (for export-related URLs).
*   **Potential Insights:** How users extract data for offline use or integration with other tools, popular export formats, types of data most frequently exported.
*   **Suggested Grouping/Type:** Feature Adoption, Data Consumption; Counter

## 3.4 User Engagement & Workflow

### a. Time Spent on Page/Task (Average)
*   **Metric Name:** `nautobot.user_activity.engagement.page_duration.seconds.avg` (tags: `page_url` or `task_name`, `user`)
*   **Description:** Average time a user spends on a specific page or performing a defined task.
*   **Data Source Ideas:** Frontend analytics (e.g., time tracking between page loads or specific UI interactions), application logs if start/end of tasks can be instrumented.
*   **Potential Insights:** Identify pages where users spend a lot of time (could be complex tasks or usability issues), understand workflow efficiency, pinpoint areas for UI/UX optimization.
*   **Suggested Grouping/Type:** Engagement, User Behavior; Timer/Distribution

### b. User Task Completion Rate
*   **Metric Name:** `nautobot.user_activity.engagement.task_completion.rate` (tags: `task_name`, `user_group`)
*   **Description:** Percentage of users who successfully complete a defined task or workflow (e.g., provisioning a new device, completing a multi-step form).
*   **Data Source Ideas:** Application-level instrumentation of defined workflows (tracking start and successful completion events).
*   **Potential Insights:** Identify bottlenecks or drop-off points in critical workflows, measure the effectiveness of UI design for specific tasks, track improvements after workflow changes.
*   **Suggested Grouping/Type:** Engagement, Workflow Efficiency; Rate/Percentage

### c. Most Active Users/Groups
*   **Metric Name:** `nautobot.user_activity.engagement.activity_score.composite` or `nautobot.user_activity.engagement.actions.count` (tags: `user`, `user_group`)
*   **Description:** Identifies users or groups with the highest overall activity (e.g., based on a composite score of logins, CRUD operations, feature usage).
*   **Data Source Ideas:** Aggregation of various other metrics (logins, CRUD counts, job executions) per user/group.
*   **Potential Insights:** Identify power users, champions, or teams that are highly reliant on Nautobot; can inform targeted support, training, or feedback sessions.
*   **Suggested Grouping/Type:** Engagement, User Behavior; Composite/Counter

---

# Plugin & Integration Activity Metrics

This section details specific metrics for understanding the usage, performance, and effectiveness of Nautobot plugins and integrations.

## 4.1 Golden Configuration Plugin Metrics

### a. Overall Compliance Status
*   **Metric Name:** `nautobot.plugin_golden_config.compliance.overall.percentage`
*   **Description:** Measures the overall percentage of devices/configurations that are compliant with their intended "golden" state.
*   **Data Source Ideas:** Golden Configuration plugin database tables (e.g., compliance reports, device status).
*   **Potential Insights:** Overall health of network configuration compliance, effectiveness of compliance policies, areas needing attention.
*   **Suggested Grouping/Type:** Plugin, Compliance; Gauge/Percentage

### b. Compliance Drift Count
*   **Metric Name:** `nautobot.plugin_golden_config.compliance.drift.detected.count` (tags: `device`, `rule_type`)
*   **Description:** Counts the number of devices or specific configuration items found to be non-compliant.
*   **Data Source Ideas:** Golden Configuration plugin database (compliance job results, non-compliant device list).
*   **Potential Insights:** Identifies specific devices or configuration areas with frequent compliance issues, helps prioritize remediation efforts.
*   **Suggested Grouping/Type:** Plugin, Compliance; Counter

### c. Time to Detect Drift
*   **Metric Name:** `nautobot.plugin_golden_config.compliance.drift_detection_time.seconds.avg`
*   **Description:** Average time taken from a configuration change (externally or internally) to its detection as non-compliance by the plugin.
*   **Data Source Ideas:** Timestamps from configuration change events (if available) and Golden Configuration plugin's detection logs.
*   **Potential Insights:** Responsiveness of the compliance monitoring system, effectiveness of detection mechanisms.
*   **Suggested Grouping/Type:** Plugin, Performance; Timer/Distribution

### d. Automated Remediation Attempts
*   **Metric Name:** `nautobot.plugin_golden_config.remediation.automated_attempts.count` (tags: `device`, `rule_type`)
*   **Description:** Counts the number of times automated remediation was attempted for non-compliant configurations.
*   **Data Source Ideas:** Golden Configuration plugin job logs, remediation script logs.
*   **Potential Insights:** Usage of automated remediation features, frequency of remediation needs.
*   **Suggested Grouping/Type:** Plugin, Automation; Counter

### e. Automated Remediation Success Rate
*   **Metric Name:** `nautobot.plugin_golden_config.remediation.automated_success.rate` (tags: `device`, `rule_type`)
*   **Description:** Percentage of automated remediation attempts that were successful.
*   **Calculation Formula:** `(Successful_Automated_Remediations / Total_Automated_Remediation_Attempts) * 100%`
*   **Data Source Ideas:** Golden Configuration plugin job logs (status of remediation jobs).
*   **Potential Insights:** Effectiveness of remediation scripts/workflows, reliability of automated fixes.
*   **Suggested Grouping/Type:** Plugin, Automation; Rate/Percentage

### f. Manual Remediation Count
*   **Metric Name:** `nautobot.plugin_golden_config.remediation.manual_intervention.count` (tags: `device`, `rule_type`)
*   **Description:** Counts instances where manual intervention was required for remediation because automation failed or was not attempted.
*   **Data Source Ideas:** Incident tickets, change management records, operator logs, Golden Configuration plugin data if manual actions can be flagged.
*   **Potential Insights:** Gaps in automation capabilities, types of issues requiring manual expertise, areas for improving automation.
*   **Suggested Grouping/Type:** Plugin, Operations; Counter

### g. Configuration Backup Status
*   **Metric Name:** `nautobot.plugin_golden_config.backup.status.rate` (tags: `device`, `status`)
*   **Description:** Success/failure rate of configuration backups performed by or integrated with the Golden Configuration plugin.
*   **Data Source Ideas:** Backup job logs within the plugin or integrated backup system.
*   **Potential Insights:** Reliability of configuration backup processes, data protection level for device configurations.
*   **Suggested Grouping/Type:** Plugin, Operations, Reliability; Rate/Percentage

### h. Most Common Reasons for Non-Compliance
*   **Metric Name:** `nautobot.plugin_golden_config.noncompliance.reason.count` (tags: `reason_code`, `rule_type`, `device_type`)
*   **Description:** Identifies and counts the most frequent reasons or types of misconfigurations causing non-compliance.
*   **Data Source Ideas:** Golden Configuration plugin compliance reports (parsed for failure reasons or specific diffs), manual analysis of non-compliant configurations.
*   **Potential Insights:** Systemic configuration issues, common human errors, areas for policy refinement or targeted training, opportunities for new automation rules.
*   **Suggested Grouping/Type:** Plugin, Compliance, Root Cause Analysis; Counter

## 4.2 SSoT Plugin Metrics

### a. Data Synchronization Job Frequency
*   **Metric Name:** `nautobot.plugin_ssot.synchronization.job_frequency.count` (tags: `source_system`, `job_name`)
*   **Description:** Counts how often data synchronization jobs are run.
*   **Data Source Ideas:** SSoT plugin job logs, Nautobot job scheduler records.
*   **Potential Insights:** How frequently data is being updated from external sources, activity levels of different integrations.
*   **Suggested Grouping/Type:** Plugin, SSoT, Scheduling; Counter

### b. Data Synchronization Job Duration
*   **Metric Name:** `nautobot.plugin_ssot.synchronization.job_duration.seconds` (tags: `source_system`, `job_name`, aggregation: `avg`, `max`, `min`)
*   **Description:** Measures the execution time of data synchronization jobs.
*   **Data Source Ideas:** SSoT plugin job logs (start and end timestamps).
*   **Potential Insights:** Performance of SSoT jobs, identification of slow or problematic integrations, impact of data volume on job duration.
*   **Suggested Grouping/Type:** Plugin, SSoT, Performance; Timer/Distribution

### c. Data Synchronization Job Success/Failure Rate
*   **Metric Name:** `nautobot.plugin_ssot.synchronization.job_status.rate` (tags: `source_system`, `job_name`, `status`)
*   **Description:** Percentage of SSoT jobs that complete successfully versus those that fail.
*   **Data Source Ideas:** SSoT plugin job logs (job status).
*   **Potential Insights:** Reliability of integrations, health of SSoT processes, identification of error-prone source systems.
*   **Suggested Grouping/Type:** Plugin, SSoT, Reliability; Rate/Percentage

### d. Number of Discrepancies Detected
*   **Metric Name:** `nautobot.plugin_ssot.discrepancy.detected.count` (tags: `source_system`, `object_type`)
*   **Description:** Counts the number of discrepancies found between Nautobot and a source system during a sync job.
*   **Data Source Ideas:** SSoT plugin logs or database (if discrepancies are logged before reconciliation).
*   **Potential Insights:** Data consistency issues between systems, effectiveness of SSoT in identifying differences, areas with high data drift.
*   **Suggested Grouping/Type:** Plugin, SSoT, Data Quality; Counter

### e. Number of Discrepancies Automatically Resolved
*   **Metric Name:** `nautobot.plugin_ssot.discrepancy.resolved_automated.count` (tags: `source_system`, `object_type`)
*   **Description:** Counts the number of detected discrepancies that were automatically resolved by SSoT jobs.
*   **Data Source Ideas:** SSoT plugin logs (actions taken by jobs, e.g., "object created," "object updated").
*   **Potential Insights:** Effectiveness of automated reconciliation logic, value of SSoT in maintaining data consistency with minimal manual effort.
*   **Suggested Grouping/Type:** Plugin, SSoT, Automation; Counter

### f. Time to Reconcile Discrepancies
*   **Metric Name:** `nautobot.plugin_ssot.discrepancy.reconciliation_time.seconds` (tags: `source_system`, `resolution_type`)
*   **Description:** Time taken to reconcile discrepancies, whether automatically or manually.
*   **Data Source Ideas:** SSoT plugin job logs (for automated), incident/task tracking systems (for manual reconciliation efforts).
*   **Potential Insights:** Efficiency of the reconciliation process, effort required for manual data alignment.
*   **Suggested Grouping/Type:** Plugin, SSoT, Performance; Timer/Distribution

### g. Data Staleness
*   **Metric Name:** `nautobot.plugin_ssot.data.staleness.hours.gauge` (tags: `source_system`, `object_type`)
*   **Description:** Measures the age of the data in Nautobot that originated from a specific source of truth (i.e., time since last successful sync).
*   **Calculation Formula:** `Current_Time - Last_Successful_Sync_Timestamp_for_Source`
*   **Data Source Ideas:** SSoT plugin job logs (last successful run timestamp per source).
*   **Potential Insights:** Timeliness of data, potential risk of using outdated information, adherence to data freshness SLAs.
*   **Suggested Grouping/Type:** Plugin, SSoT, Data Quality; Gauge

### h. Objects Created/Updated/Deleted by SSoT Jobs
*   **Metric Name:** `nautobot.plugin_ssot.objects_changed.count` (tags: `source_system`, `object_type`, `action`)
*   **Description:** Counts the number of objects created, updated, or deleted in Nautobot by SSoT jobs.
*   **Data Source Ideas:** SSoT plugin job logs (summary of changes), Nautobot change logs (filtered by SSoT user/source).
*   **Potential Insights:** Impact of each SSoT integration on Nautobot data, volume of changes processed, types of objects most affected by SSoT.
*   **Suggested Grouping/Type:** Plugin, SSoT, Data Management; Counter

## 4.3 Device Lifecycle Management (DLM) Plugin Metrics

### a. Time to Provision New Device
*   **Metric Name:** `nautobot.plugin_dlm.provisioning.duration.seconds` (tags: `device_type`, `site`, aggregation: `avg`, `max`, `min`)
*   **Description:** Measures the time taken from the initial request or 'planned' state of a device to its 'active' or 'in service' status.
*   **Data Source Ideas:** DLM plugin data (timestamps for lifecycle stage changes), ticketing system (request creation date), Nautobot device status and operational state.
*   **Potential Insights:** Efficiency of the device provisioning process, bottlenecks in onboarding, impact of automation on provisioning speed.
*   **Suggested Grouping/Type:** Plugin, DLM, Performance; Timer/Distribution

### b. Devices per Lifecycle Stage
*   **Metric Name:** `nautobot.plugin_dlm.inventory.devices_by_stage.gauge` (tags: `stage_name`, `device_type`)
*   **Description:** Counts the number of devices currently in each defined lifecycle stage (e.g., 'planned', 'provisioning', 'active', 'decommissioning', 'retired').
*   **Data Source Ideas:** DLM plugin's internal state management for devices, Nautobot device status if mapped to lifecycle stages.
*   **Potential Insights:** Current inventory status, flow of devices through the lifecycle, potential backlogs in certain stages (e.g., many devices awaiting decommissioning).
*   **Suggested Grouping/Type:** Plugin, DLM, Inventory; Gauge

### c. Errors/Fallouts During Lifecycle Transitions
*   **Metric Name:** `nautobot.plugin_dlm.transition.error.count` (tags: `from_stage`, `to_stage`, `error_type`)
*   **Description:** Counts the number of errors or fallouts occurring when a device attempts to transition from one lifecycle stage to another.
*   **Data Source Ideas:** DLM plugin logs, job logs associated with lifecycle automation, incident tickets related to provisioning/decommissioning failures.
*   **Potential Insights:** Reliability of lifecycle processes, common failure points, stages prone to issues, impact on operational stability.
*   **Suggested Grouping/Type:** Plugin, DLM, Reliability; Counter

### d. Lifecycle Process Adherence
*   **Metric Name:** `nautobot.plugin_dlm.process.adherence.rate` (tags: `device_type`, `process_name`)
*   **Description:** Percentage of devices that follow the defined lifecycle process without deviations or manual overrides.
*   **Data Source Ideas:** DLM plugin logs (tracking expected vs. actual transitions), audit trails, comparison of device states against defined policies.
*   **Potential Insights:** Effectiveness of defined processes, areas where processes are bypassed, compliance with operational standards.
*   **Suggested Grouping/Type:** Plugin, DLM, Compliance; Rate/Percentage

### e. Time Spent in Each Lifecycle Stage
*   **Metric Name:** `nautobot.plugin_dlm.stage.duration.days.avg` (tags: `stage_name`, `device_type`)
*   **Description:** Average, maximum, or minimum time devices spend in each lifecycle stage.
*   **Data Source Ideas:** DLM plugin data (timestamps for entry and exit of each stage per device).
*   **Potential Insights:** Identifies bottlenecks where devices get stuck, helps optimize stage durations, informs capacity planning for future stages.
*   **Suggested Grouping/Type:** Plugin, DLM, Performance; Timer/Distribution

### f. Automation Rate per Lifecycle Stage
*   **Metric Name:** `nautobot.plugin_dlm.stage.automation.rate` (tags: `stage_name`, `task_name`)
*   **Description:** Percentage of tasks or steps within each lifecycle stage that are automated versus manual.
*   **Data Source Ideas:** DLM plugin configuration (defining automated vs. manual steps), job logs for automated tasks, manual tracking or surveys for manual steps.
*   **Potential Insights:** Level of automation achieved in device lifecycle management, opportunities for further automation, efficiency gains from automation at each stage.
*   **Suggested Grouping/Type:** Plugin, DLM, Automation; Rate/Percentage

## 4.4 General Plugin & Job Metrics

These metrics are applicable to any job executed within Nautobot, including those from specific plugins mentioned above or custom jobs. They can be dimensioned by `plugin_name`, `job_class_path` (or `job_name`), `user` (if user-initiated).

### a. Job Volume/Count
*   **Metric Name:** `nautobot.job_execution.total.count` (tags: `plugin_name`, `job_name`, `user`, `trigger`)
*   **Description:** Total number of jobs run, which can be aggregated per plugin, per job type, per user, or by how it was triggered.
*   **Data Source Ideas:** Nautobot job result database, Celery backend (if jobs are processed via Celery).
*   **Potential Insights:** Overall system activity for automated tasks, most frequently used jobs/plugins, user reliance on specific jobs, load patterns based on trigger type.
*   **Suggested Grouping/Type:** Job, Performance; Counter

### b. Job Results
*   **Metric Name:** `nautobot.job_execution.status.rate` (tags: `plugin_name`, `job_name`, `status`)
*   **Description:** Counts and rates of job outcomes (Success, Failure, Warning, Info, etc.).
*   **Data Source Ideas:** Nautobot job result database.
*   **Potential Insights:** Reliability of specific jobs or plugins, identification of problematic jobs, overall health of the automation platform.
*   **Suggested Grouping/Type:** Job, Reliability; Rate/Percentage

### c. Job Execution Time
*   **Metric Name:** `nautobot.job_execution.duration.seconds` (tags: `plugin_name`, `job_name`, aggregations: `avg`, `max`, `min`, `p95`)
*   **Description:** Measures the execution time of jobs.
*   **Data Source Ideas:** Nautobot job result database (start and end timestamps).
*   **Potential Insights:** Performance of jobs, identification of slow or inefficient jobs, impact of data volume or system load on job execution, SLA tracking for job completion.
*   **Suggested Grouping/Type:** Job, Performance; Timer/Distribution

### d. Job Throughput
*   **Metric Name:** `nautobot.job_execution.throughput.per_minute.count` (tags: `plugin_name`, `job_name`)
*   **Description:** Number of jobs of a specific type processed per unit of time (e.g., per minute, per hour).
*   **Data Source Ideas:** Aggregation of job counts from Nautobot job result database over time windows.
*   **Potential Insights:** Processing capacity of the job execution system, performance under load, efficiency of job workers.
*   **Suggested Grouping/Type:** Job, Performance; Rate

### e. Resource Consumption per Job
*   **Metric Name:** `nautobot.job_execution.resource.cpu.percentage`, `nautobot.job_execution.resource.memory.bytes` (tags: `plugin_name`, `job_name`, `worker_node`)
*   **Description:** CPU and Memory consumed by a job during its execution. This is often more easily measured at the Celery worker level.
*   **Data Source Ideas:** Celery monitoring tools (e.g., Flower), host-level monitoring on worker nodes (correlated with job execution times). Might require advanced instrumentation.
*   **Potential Insights:** Identification of resource-intensive jobs, capacity planning for worker nodes, optimization opportunities for job code.
*   **Suggested Grouping/Type:** Job, Performance, Resource Utilization; Gauge/Distribution

### f. Job Scheduling Delays
*   **Metric Name:** `nautobot.job_execution.scheduling_delay.seconds` (tags: `plugin_name`, `job_name`, `queue_name`)
*   **Description:** Time difference between when a job was scheduled to start and when it actually began execution.
*   **Data Source Ideas:** Nautobot job result database (scheduled time vs. start time), Celery task event stream (task received vs. task started events).
*   **Potential Insights:** Worker contention or saturation, queue backlogs, efficiency of the job scheduling and dispatching mechanism.
*   **Suggested Grouping/Type:** Job, Performance, Scheduling; Timer/Distribution

---

# Metric Naming Conventions and Groupings

This section establishes a clear and consistent strategy for naming metrics using a hierarchical dot-notation and proposes groupings for dashboards and reporting, including a tagging strategy. A consistent naming and grouping strategy is crucial for discoverability, organization, and efficient use of metrics in dashboards, alerting, and analysis.

## 5.1 Naming Convention

We propose a hierarchical dot-notation structure for naming metrics. This structure provides a predictable and understandable way to identify and categorize metrics.

**Structure:**
`nautobot.<category>.<subcategory>.<action_or_object>.<specific_detail>.<unit_or_aggregation>`

**Components:**

*   `nautobot`: This is a constant prefix for all metrics originating from or related to the Nautobot ecosystem. It serves as the top-level namespace.
*   `<category>`: Represents the broad area or primary focus of the metric. This aligns with the major sections previously defined in this document.
    *   Examples: `roi`, `user_activity`, `system_performance`, `plugin_golden_config`, `plugin_ssot`, `plugin_dlm`, `job_execution`.
    *   For plugins, the format `plugin_<plugin_name>` should be used (e.g., `plugin_golden_config`).
*   `<subcategory>`: Provides a more specific grouping within the category. This helps to further narrow down the metric's context.
    *   Examples: `cost_savings`, `authentication`, `object_management`, `compliance`, `synchronization`, `provisioning`, `celery_workers`.
*   `<action_or_object>`: Describes the specific action being measured or the primary entity the metric pertains to.
    *   Examples: `login`, `session`, `object_creation`, `device_count`, `drift_detection`, `job_completion`, `task_throughput`, `page_view`.
*   `<specific_detail>`: Offers further granularity if the above components are not sufficient to uniquely identify the metric or its specific aspect. This can include status, type, or other relevant attributes.
    *   Examples: `success`, `failure`, `by_user`, `status_compliant`, `type_firewall`, `trigger_manual`.
    *   This component can be omitted if not needed for clarity.
*   `<unit_or_aggregation>`: Specifies the unit of measurement or the type of aggregation applied to the metric.
    *   **Units:** `count` (for discrete events), `seconds` (for time), `bytes` (for size), `percentage` (for ratios, 0-100), `gauge` (for point-in-time values that can go up or down), `items` (generic count).
    *   **Aggregations (often applied to timers/distributions):** `avg` (average), `max` (maximum), `min` (minimum), `p95` (95th percentile), `sum` (total sum, often implied for counters). For counters, `count` is typically used. For gauges, `gauge` is used. For timers/summaries, the aggregation (e.g. `avg`, `p95`) is often part of the metric name or handled by the monitoring system's query language. Explicitly using `count` for counters and `gauge` for gauges is recommended.

**Rules & Guidelines:**

*   **Lowercase:** All components of the metric name should be in lowercase to ensure consistency and avoid case-sensitivity issues in monitoring systems.
*   **Underscores for Separation:** Use underscores (`_`) to separate words *within* a component (e.g., `user_activity`, `object_management`, `time_saved`). Do not use underscores to separate the main components themselves; dots serve this purpose.
*   **Dot Notation for Hierarchy:** Use dots (`.`) to separate the hierarchical components of the metric name as defined in the structure.
*   **Consistency:** Use consistent terminology for the same concepts across different metrics. For example, if `login` is used for authentication, avoid using `signin` elsewhere for the same concept.
*   **Clarity and Descriptiveness:** Names should be clear and descriptive enough to be understood without needing extensive documentation for each metric.
*   **Avoid Excessive Length:** While descriptiveness is important, try to keep metric names reasonably concise. Components can be omitted if they don't add necessary clarity or if the metric is already specific enough.
*   **Plugin Specificity:** For metrics originating from a specific plugin, the `<category>` should clearly indicate the plugin, e.g., `plugin_golden_config`, `plugin_ssot`.
*   **Units for Timers:** For timer metrics, explicitly include the time unit (e.g., `seconds`, `milliseconds`) in the unit/aggregation component if the monitoring system doesn't automatically handle base units. However, many systems (like Prometheus) prefer base units (seconds) and handle conversions in queries. `seconds` is a good default.
*   **Counters:** Counters should typically end with `.count`.
*   **Gauges:** Gauges should typically end with `.gauge`.
*   **Rates:** While "rate" can be a conceptual type, the metric name itself might be a `count` or `gauge` from which a rate is calculated (e.g., `nautobot.user_activity.authentication.login.success.count` can be used to calculate a login rate).

**Examples (adapting previously defined metrics):**

1.  **User Login Success:**
    *   Old: `user.login.success.count`
    *   New: `nautobot.user_activity.authentication.login.success.count`
2.  **Golden Configuration Compliance Drift:**
    *   Old: `plugin.golden_config.compliance.drift.count`
    *   New: `nautobot.plugin_golden_config.compliance.drift.detected.count`
3.  **ROI Time Saved per Task:**
    *   Old: Time Saved per Automated Task (conceptual)
    *   New: `nautobot.roi.efficiency_gains.task_automation.time_saved.hours.avg` (assuming an average) or `nautobot.roi.efficiency_gains.task_automation.time_saved.hours` (if reported per instance)
4.  **SSoT Job Duration:**
    *   Old: `plugin.ssot.job.duration.seconds`
    *   New: `nautobot.plugin_ssot.synchronization.job.duration.seconds.avg` (for average duration)
5.  **Object Creation Count (Devices):**
    *   Old: `object.create.count` (dimension: `object_type:device`)
    *   New: `nautobot.user_activity.object_management.device.creation.count` (tags/labels would specify UI/API)
6.  **Job Execution Duration (General):**
    *   Old: `job.execution.duration.seconds`
    *   New: `nautobot.job_execution.generic.duration.seconds.p95` (example for 95th percentile)
7.  **Active User Sessions:**
    *   Old: `user.session.active.gauge`
    *   New: `nautobot.user_activity.session_management.active_sessions.gauge`
8.  **DLM Time to Provision Device:**
    *   Old: `plugin.dlm.provisioning.duration.seconds`
    *   New: `nautobot.plugin_dlm.provisioning.device.time_to_active.seconds.avg`
9.  **API Request Count:**
    *   Conceptual: Volume of API requests
    *   New: `nautobot.system_performance.api.request.total.count` (can be dimensioned by endpoint, method, status)
10. **Reduced Operational Costs (ROI):**
    *   Conceptual: Reduced Operational Costs
    *   New: `nautobot.roi.cost_savings.operational.reduction.dollars.total` (assuming a total sum)

## 5.2 Metric Groupings for Dashboards & Reporting

Effective grouping and tagging of metrics are essential for creating meaningful dashboards, enabling flexible data exploration, and configuring targeted alerting. This allows different stakeholders to access relevant views of the data.

**Purpose of Groupings & Tagging:**

*   **Organization:** Structure dashboards into logical sections or tabs.
*   **Discoverability:** Help users find relevant metrics quickly.
*   **Filtering & Aggregation:** Allow for dynamic filtering and aggregation of metrics based on various dimensions (e.g., show all metrics for a specific plugin, or all compliance-related metrics).
*   **Targeted Alerting:** Define alert rules based on specific groups or tags (e.g., alert on any job failure for production SSoT integrations).
*   **Role-Based Views:** Facilitate the creation of dashboards tailored to different roles (e.g., executive overview, operations team dashboard, plugin developer view).

**Proposed High-Level Dashboard Groups:**

These groups can serve as tabs in a comprehensive Nautobot monitoring dashboard or as separate, focused dashboards:

1.  **Executive ROI & Business Value:**
    *   Focus: Metrics demonstrating cost savings, efficiency gains, and overall business impact.
    *   Key Metrics: `nautobot.roi.*`, selected business impact metrics.
2.  **User Engagement & Activity:**
    *   Focus: How users are interacting with Nautobot, popular features, and overall adoption.
    *   Key Metrics: `nautobot.user_activity.*` (logins, CRUD operations, feature usage).
3.  **Automation & Job Performance:**
    *   Focus: Performance and reliability of all automated tasks and jobs running within or initiated by Nautobot.
    *   Key Metrics: `nautobot.job_execution.*`, `nautobot.plugin_*/job/*`, `nautobot.plugin_*/automation/*`.
4.  **Golden Configuration & Compliance Health:**
    *   Focus: Status of network device configuration compliance and the performance of the Golden Configuration plugin.
    *   Key Metrics: `nautobot.plugin_golden_config.*`.
5.  **SSoT & Data Integrity:**
    *   Focus: Performance and effectiveness of SSoT integrations, data synchronization status, and data consistency.
    *   Key Metrics: `nautobot.plugin_ssot.*`.
6.  **Device Lifecycle Operations (DLM):**
    *   Focus: Efficiency and status of device lifecycle management processes.
    *   Key Metrics: `nautobot.plugin_dlm.*`.
7.  **Nautobot System Health & Performance:**
    *   Focus: Core application performance, resource utilization, and stability of the Nautobot platform itself. (Assumes system performance metrics like API response times, worker stats, DB performance are also collected under `nautobot.system_performance.*`).
    *   Key Metrics: `nautobot.system_performance.*` (e.g., API requests, Celery worker stats, database connection pool).

**Tagging/Labeling Strategy:**

Using tags (or labels in Prometheus terminology) allows for multi-dimensional filtering and aggregation, offering more flexibility than purely hierarchical naming. Metrics should be enriched with relevant tags at the source.

**Standard Tags to Implement:**

*   `metric_category`: Broad functional area.
    *   Examples: `roi`, `user_activity`, `plugin_golden_config`, `plugin_ssot`, `plugin_dlm`, `job_execution`, `system_performance`.
    *   *This often aligns with the `<category>` component of the metric name.*
*   `metric_type`: The fundamental type of the metric.
    *   Examples: `counter` (monotonically increasing), `gauge` (can go up or down), `timer` (measures duration, often exposed as a summary or histogram), `rate`, `percentage`.
*   `plugin_name`: If the metric is specific to a plugin.
    *   Examples: `golden_config`, `ssot_aci`, `device_lifecycle_mgmt`, `welcome_wizard_plugin`.
    *   Allows filtering for all metrics related to a particular plugin.
*   `object_type`: For metrics related to specific Nautobot models or data types.
    *   Examples: `device`, `ip_address`, `vlan`, `prefix`, `circuit`, `site`, `interface`.
    *   Useful for `nautobot.user_activity.object_management.*` metrics.
*   `job_name` or `job_class_path`: The specific name or class path of a job being executed.
    *   Examples: `IntendedMerger`, `SyncDeviceDataFromServiceNow`, `DeviceConfigurationBackup`.
*   `user_name`: (Use with caution due to cardinality) The user who initiated an action.
    *   Could be useful for detailed audit or activity tracking but can lead to high cardinality in the monitoring system. Consider `user_group` as a more common alternative.
*   `user_group`: The group(s) the acting user belongs to.
    *   Examples: `network_admins`, `provisioning_team`, `read_only_users`.
*   `source_system`, `target_system`: For SSoT jobs, indicating the origin and destination of data.
    *   Examples: `source_system:servicenow`, `target_system:aci`.
*   `status`: For metrics that represent outcomes.
    *   Examples: `success`, `failure`, `compliant`, `non_compliant`, `error_4xx`, `error_5xx`.
*   `access_method` or `source`: How the action was initiated.
    *   Examples: `ui`, `api`, `cli`, `system_scheduled`.

By combining the hierarchical naming convention with this tagging strategy, Nautobot metrics can be effectively organized, queried, and visualized to provide comprehensive insights into its operation and value.

---

# Conceptual Dashboard Designs (Suite of 20)

This section outlines 20 conceptual dashboard designs for visualizing Nautobot metrics. Each design includes a title, its purpose/focus, the primary target audience, and examples of key metrics with suggested visualizations.

---

## 6.1 Executive ROI & Business Value Dashboard

*   **Purpose/Focus:** To provide a high-level overview of the tangible financial and operational benefits derived from implementing and utilizing Nautobot, focusing on cost savings, efficiency gains, and overall business value.
*   **Target Audience:** Executives, Business Unit Leaders, IT Management.
*   **Key Metrics & Visualizations (Examples):**
    1.  `nautobot.roi.cost_savings.operational.reduction.dollars.total` - Total Operational Cost Reduction (YTD, Quarterly) (Big Number, Trend Line Chart)
    2.  `nautobot.roi.efficiency_gains.task_automation.time_saved.hours.sum` - Total Hours Saved via Automation (YTD, Quarterly) (Big Number, Trend Line Chart)
    3.  `nautobot.roi.cost_savings.tool_consolidation.dollars.annual` - Annualized Tooling Cost Savings (Gauge / Big Number)
    4.  `nautobot.roi.cost_avoidance.outage_prevention.dollars.sum` - Estimated Cost Avoided (e.g., from outage prevention) (Big Number)
    5.  `nautobot.business_impact.service_delivery.time_reduction.percentage.avg` - Average Service Delivery Time Reduction % (Gauge)
    6.  Key Automation Projects ROI (e.g., GC ROI, SSoT ROI - calculated values) (Table with summary stats)
    7.  Overall Automation Adoption Rate (`nautobot.roi.efficiency_gains.automation_adoption.percentage`) (Gauge)

---

## 6.2 Automation Program Health Dashboard

*   **Purpose/Focus:** To monitor the overall health, adoption, and success of key automation initiatives powered by Nautobot, including Golden Configuration, SSoT, and DLM.
*   **Target Audience:** IT Management, Automation Program Leads, Engineering Managers.
*   **Key Metrics & Visualizations (Examples):**
    1.  `nautobot.roi.efficiency_gains.automation_adoption.percentage` - Overall Automation Adoption Rate (Gauge, Time Series Line Chart)
    2.  `nautobot.plugin_golden_config.compliance.overall.percentage` - Golden Configuration Overall Compliance (Gauge, Time Series Line Chart)
    3.  `nautobot.plugin_ssot.job.status.rate` (tag: `status:success`) - SSoT Job Success Rate (by source system) (Bar Chart / Table)
    4.  `nautobot.plugin_dlm.stage.automation.rate` - DLM Automation Rate per Stage (Bar Chart)
    5.  `nautobot.job_execution.generic.status.rate` (tag: `status:success`) - Overall Job Success Rate (Time Series Line Chart)
    6.  `nautobot.user_activity.feature_usage.job_execution_by_trigger.count` (tag: `trigger:automated`) - Count of Automated Job Executions (Time Series Bar Chart)
    7.  Reduction in Manual Error Rates (conceptual, `nautobot.roi.efficiency_gains.manual_error_reduction.percentage`) (Time Series Line Chart)

---

## 6.3 Risk & Compliance Overview Dashboard

*   **Purpose/Focus:** To provide management with a consolidated view of the organization's risk posture and compliance status as managed and monitored by Nautobot.
*   **Target Audience:** Executives, Risk Management Team, Compliance Officers, Security Team, IT Management.
*   **Key Metrics & Visualizations (Examples):**
    1.  `nautobot.plugin_golden_config.compliance.overall.percentage` - Overall Device Compliance Rate (Gauge, Trend Line)
    2.  `nautobot.plugin_golden_config.compliance.drift.detected.count` - High Severity Compliance Drifts (past 7 days) (Big Number, Table)
    3.  `nautobot.plugin_ssot.data.staleness.hours.avg` (by critical source system) - Data Staleness for Critical Systems (Bar Chart / Table)
    4.  `nautobot.plugin_dlm.process.adherence.rate` - DLM Process Adherence Rate (Gauge)
    5.  `nautobot.system_performance.security.failed_login_attempts.count` - Failed Login Attempts (past 24h/7d) (Big Number, Time Series)
    6.  Audit Trail - Critical Changes Count (e.g., `nautobot.user_activity.object_management.critical_object.update.count`) (Time Series Bar Chart)
    7.  `nautobot.plugin_golden_config.remediation.automated.success.rate` - Automated Compliance Remediation Success Rate (Gauge)

---

## 6.4 Nautobot Platform Health & Usage Dashboard

*   **Purpose/Focus:** To monitor the overall health, performance, and usage patterns of the Nautobot platform itself.
*   **Target Audience:** Platform Admins, Nautobot Support Team, IT Operations.
*   **Key Metrics & Visualizations (Examples):**
    1.  `nautobot.system_performance.api.request.total.count` (per minute/hour) - API Request Rate (Time Series Line Chart)
    2.  `nautobot.system_performance.api.response_time.seconds.p95` - API Response Time (P95) (Time Series Line Chart)
    3.  `nautobot.system_performance.application.error.rate` (HTTP 5xx) - Application Error Rate (Time Series Line Chart, Gauge)
    4.  `nautobot.user_activity.session_management.active_sessions.gauge` - Active User Sessions (Time Series Line Chart, Gauge)
    5.  `nautobot.system_performance.celery_workers.task_queue_length.gauge` - Celery Task Queue Length (by queue) (Time Series Line Chart)
    6.  `nautobot.system_performance.database.connection_pool.utilization.percentage` - Database Connection Pool Utilization (Gauge)
    7.  `nautobot.user_activity.feature_usage.page_view.top_pages.count` - Top 10 Most Viewed Pages/Features (Bar Chart)

---

## 6.5 User Activity & Engagement Dashboard

*   **Purpose/Focus:** To provide detailed insights into how users are interacting with Nautobot, which features they use, and overall engagement levels.
*   **Target Audience:** Platform Admins, Product Managers (for Nautobot), UX Designers, Training Teams.
*   **Key Metrics & Visualizations (Examples):**
    1.  `nautobot.user_activity.authentication.login.success.count` (Daily/Weekly Active Users) (Time Series Bar Chart)
    2.  `nautobot.user_activity.session_management.session_duration.seconds.avg` - Average Session Duration (Time Series Line Chart)
    3.  `nautobot.user_activity.object_management.object.creation.count` (by object type) - Object Creation Trends (Stacked Bar Chart)
    4.  `nautobot.user_activity.object_management.object.read.count` (by object type) - Object View Trends (Stacked Bar Chart)
    5.  `nautobot.user_activity.feature_usage.filter_usage.top_filters.count` - Top Used Filters (Bar Chart or Table)
    6.  `nautobot.user_activity.feature_usage.job_execution.by_user_group.count` - Job Executions by User Group (Pie Chart / Bar Chart)
    7.  `nautobot.user_activity.adoption.new_feature_usage.count` (for specific new features) - New Feature Adoption Rate (Time Series Line Chart)

---

## 6.6 Golden Configuration - Compliance Deep Dive

*   **Purpose/Focus:** To provide a detailed view of device configuration compliance, enabling engineers to identify non-compliant devices, understand drift patterns, and track remediation progress.
*   **Target Audience:** Network Engineering, Network Operations, Security Compliance Team.
*   **Key Metrics & Visualizations (Examples):**
    1.  `nautobot.plugin_golden_config.compliance.overall.percentage` - Overall Compliance % (Gauge)
    2.  Non-Compliant Devices List (Table: Device, Site, Compliance Status, Last Checked)
    3.  `nautobot.plugin_golden_config.compliance.drift.detected.count` (by device/rule/severity over time) - Compliance Drift Trends (Stacked Bar Chart / Line Chart)
    4.  `nautobot.plugin_golden_config.noncompliance.reason.top_reasons.count` - Top Reasons for Non-Compliance (Bar Chart)
    5.  `nautobot.plugin_golden_config.remediation.automated.success.rate` (per rule/device type) - Remediation Success Rate (Bar Chart)
    6.  `nautobot.plugin_golden_config.compliance.time_to_detect_drift.seconds.avg` - Avg. Time to Detect Drift (Time Series Line Chart)
    7.  Compliance Status per Git Repository/Branch (if applicable) (Table)

---

## 6.7 Golden Configuration - Operational Dashboard

*   **Purpose/Focus:** To monitor the operational aspects of the Golden Configuration plugin, including backup status, job performance, and common issues.
*   **Target Audience:** Network Operations, Platform Admins managing GC.
*   **Key Metrics & Visualizations (Examples):**
    1.  `nautobot.plugin_golden_config.job.backup.status.rate` (success/failure) - Configuration Backup Job Status (Pie Chart / Bar Chart over time)
    2.  `nautobot.plugin_golden_config.job.compliance_check.status.rate` - Compliance Check Job Status (Pie Chart / Bar Chart over time)
    3.  `nautobot.plugin_golden_config.job.remediation.duration.seconds.avg` - Average Remediation Job Duration (Time Series Line Chart)
    4.  `nautobot.plugin_golden_config.job.execution.total.count` (Backup, Compliance, Remediation) - Job Volume Trends (Stacked Bar Chart)
    5.  Top Failing Backup/Compliance Jobs (Table: Job ID, Device, Error Message)
    6.  `nautobot.plugin_golden_config.settings.intended_vs_actual_config_drift.count` - Devices with Intended vs Actual Config Drift (Big Number)
    7.  `nautobot.plugin_golden_config.resource.cpu.percentage`, `nautobot.plugin_golden_config.resource.memory.bytes` - Resource Usage by GC Jobs (Time Series)

---

## 6.8 SSoT - Data Reconciliation & Integrity Dashboard

*   **Purpose/Focus:** To monitor the health and effectiveness of Single Source of Truth (SSoT) integrations, focusing on data synchronization status, discrepancies, and data staleness.
*   **Target Audience:** Platform Admins, Data Stewards, Integration Specialists, Network Operations.
*   **Key Metrics & Visualizations (Examples):**
    1.  `nautobot.plugin_ssot.synchronization.job.status.rate` (by source system, success/failure) - SSoT Job Success Rate (Bar Chart, Table)
    2.  `nautobot.plugin_ssot.synchronization.job.duration.seconds.avg` (by source system) - Average SSoT Job Duration (Time Series / Bar Chart)
    3.  `nautobot.plugin_ssot.discrepancy.detected.count` (by source system, object type) - Discrepancies Detected (Stacked Bar Chart / Heatmap)
    4.  `nautobot.plugin_ssot.discrepancy.resolved.automated.count` (by source system) - Discrepancies Automatically Resolved (Time Series Line Chart)
    5.  `nautobot.plugin_ssot.data.staleness.hours.gauge` (by source system, critical object types) - Data Staleness (Gauge / Bar Chart)
    6.  Top SSoT Job Failures (Table: Job Name, Source System, Error, Last Run)
    7.  `nautobot.plugin_ssot.synchronization.manual_intervention.required.count` - Manual Interventions Required (Counter / Trend Line)

---

## 6.9 SSoT - Impact Analysis Dashboard

*   **Purpose/Focus:** To understand the impact of SSoT jobs on Nautobot's data, tracking objects created, updated, or deleted by various integrations.
*   **Target Audience:** Platform Admins, Data Stewards, Network Architects.
*   **Key Metrics & Visualizations (Examples):**
    1.  `nautobot.plugin_ssot.objects_changed.created.count` (by SSoT source, object type) - Objects Created by SSoT (Time Series Stacked Bar Chart)
    2.  `nautobot.plugin_ssot.objects_changed.updated.count` (by SSoT source, object type) - Objects Updated by SSoT (Time Series Stacked Bar Chart)
    3.  `nautobot.plugin_ssot.objects_changed.deleted.count` (by SSoT source, object type) - Objects Deleted by SSoT (Time Series Stacked Bar Chart)
    4.  Net Data Change Volume by SSoT Source (Sankey Diagram showing flow of data changes)
    5.  Most Active SSoT Integrations (by volume of changes) (Bar Chart)
    6.  Data Change Rate by Object Type (due to SSoT) (Time Series Line Chart)
    7.  Rollback/Reversion Activity Post-SSoT Sync (if tracked) (Counter)

---

## 6.10 Device Lifecycle Management (DLM) - Efficiency Dashboard

*   **Purpose/Focus:** To measure the efficiency of device lifecycle processes, focusing on time taken for key stages and the level of automation achieved.
*   **Target Audience:** Network Operations Managers, Provisioning Teams, Automation Team.
*   **Key Metrics & Visualizations (Examples):**
    1.  `nautobot.plugin_dlm.provisioning.device.time_to_active.seconds.avg` - Average Time to Provision New Device (Time Series Line Chart, Gauge)
    2.  `nautobot.plugin_dlm.decommissioning.device.time_to_retired.seconds.avg` - Average Time to Decommission Device (Time Series Line Chart)
    3.  `nautobot.plugin_dlm.stage.duration.avg.days` (by stage: planned, staging, active, etc.) - Avg. Time Spent in Each Lifecycle Stage (Bar Chart)
    4.  `nautobot.plugin_dlm.stage.automation.rate` (by stage) - Automation Rate per Lifecycle Stage (Stacked Bar Chart: Automated vs Manual Steps)
    5.  Throughput of Device Provisioning/Decommissioning (devices per week/month) (Bar Chart)
    6.  Manual Touchpoints per Lifecycle Process (Heatmap or Table)
    7.  Cost Savings from DLM Automation (calculated, e.g., `nautobot.roi.efficiency_gains.dlm_automation.dollars.sum`) (Big Number)

---

## 6.11 DLM - Operational Status Dashboard

*   **Purpose/Focus:** To provide an operational overview of the device lifecycle, including current inventory status by stage, transition errors, and upcoming scheduled activities.
*   **Target Audience:** Network Operations, Provisioning Teams, Asset Management.
*   **Key Metrics & Visualizations (Examples):**
    1.  `nautobot.plugin_dlm.inventory.devices_by_stage.gauge` (Planned, Staging, Active, Decommissioning, Retired) (Pie Chart or Bar Chart)
    2.  `nautobot.plugin_dlm.transition.error.count` (by stage transition, error type) - Errors During Lifecycle Transitions (Bar Chart / Table)
    3.  Upcoming Scheduled Decommissions/Activations (Next 30 days) (Table / Calendar View)
    4.  Devices Overdue for Next Lifecycle Stage (e.g., planned but not provisioned on schedule) (Table)
    5.  `nautobot.plugin_dlm.process.adherence.rate` - Lifecycle Process Adherence Rate (Gauge)
    6.  Devices Awaiting Parts/Information (if this status is tracked within DLM) (Counter)
    7.  Successfully Completed Lifecycle Transitions (past 7 days, by type) (Bar Chart)

---

## 6.12 Job Execution & Automation Performance Dashboard

*   **Purpose/Focus:** To monitor the overall performance and reliability of all jobs and automations running within Nautobot.
*   **Target Audience:** Platform Admins, Automation Team, Operations Team.
*   **Key Metrics & Visualizations (Examples):**
    1.  `nautobot.job_execution.generic.status.rate` (success/failure overall) - Overall Job Success Rate (Gauge, Time Series Line Chart)
    2.  `nautobot.job_execution.generic.duration.seconds.avg` - Average Job Execution Time (Time Series Line Chart)
    3.  `nautobot.job_execution.generic.duration.seconds.p95` - P95 Job Execution Time (Time Series Line Chart)
    4.  `nautobot.job_execution.generic.throughput.per_minute.count` - Job Throughput (jobs/min) (Time Series Line Chart)
    5.  Top 10 Longest Running Jobs (Table: Job Name, Avg Duration, Count)
    6.  Top 10 Most Frequently Failing Jobs (Table: Job Name, Failure Count, Last Error)
    7.  `nautobot.job_execution.generic.scheduling_delay.seconds.avg` - Average Job Scheduling Delay (Time Series Line Chart)

---

## 6.13 Ansible Automation (via Nautobot) Performance

*   **Purpose/Focus:** To specifically track the performance and outcomes of Ansible automation jobs that are integrated with or triggered by Nautobot.
*   **Target Audience:** Automation Team, Network Engineers using Ansible.
*   **Key Metrics & Visualizations (Examples):**
    1.  Ansible Playbook Success Rate (via Nautobot Jobs) (Gauge, Time Series, dimensioned by playbook name)
    2.  Ansible Task Duration (P95, Avg - from playbook runs triggered by Nautobot) (Time Series, dimensioned by playbook/task)
    3.  `nautobot.job_execution.ansible.changes_made.count` - Number of Configuration Changes Made by Ansible (via Nautobot) (Time Series Bar Chart)
    4.  `nautobot.job_execution.ansible.failed_tasks.count` (by task name, playbook name) - Ansible Failed Task Count (Bar Chart / Table)
    5.  Host Unreachability in Ansible Runs (from Nautobot) (Counter / Trend)
    6.  Most Frequent Ansible Errors (from Nautobot job logs) (Table)
    7.  Ansible Job Execution Volume (triggered by Nautobot) (Time Series Bar Chart)

---

## 6.14 CI/CD Pipeline Integration Dashboard

*   **Purpose/Focus:** To monitor the interaction and impact of Nautobot on CI/CD pipelines, especially where Nautobot data (e.g., intended state) drives pipeline actions.
*   **Target Audience:** DevOps Team, Automation Team, Network Engineers.
*   **Key Metrics & Visualizations (Examples):**
    1.  `nautobot.integration.cicd.pipeline_trigger.from_nautobot_event.count` - CI/CD Pipelines Triggered by Nautobot Events (Time Series Bar Chart)
    2.  `nautobot.integration.cicd.data_validation.success.rate` (for data pulled from Nautobot) - Pipeline Data Validation Success Rate (Gauge, Time Series)
    3.  `nautobot.integration.cicd.deployment.using_nautobot_data.duration.seconds.avg` - Avg. Deployment Time for Nautobot-driven Pipelines (Time Series)
    4.  `nautobot.integration.cicd.deployment.using_nautobot_data.failure.rate` - Failure Rate of Deployments Using Nautobot Data (Gauge, Time Series)
    5.  Frequency of Rollbacks due to Nautobot Data Issues in CI/CD (Counter)
    6.  Types of CI/CD Jobs Utilizing Nautobot Data (e.g., pre-checks, deployments, post-checks) (Pie Chart)
    7.  Data Sync Time between Nautobot and CI/CD tools (if applicable) (Time Series)

---

## 6.15 Network Services Health (derived from Nautobot data)

*   **Purpose/Focus:** To leverage Nautobot's SSoT data to provide insights into the health and utilization of key network services.
*   **Target Audience:** Network Operations, Network Planners, Capacity Management.
*   **Key Metrics & Visualizations (Examples):**
    1.  `nautobot.data_derived.ipam.prefix_utilization.percentage.avg` (by VRF/Region) - Average Prefix Utilization (Heatmap / Bar Chart)
    2.  `nautobot.data_derived.ipam.available_ips.count` (by critical prefix/pool) - Available IP Addresses in Critical Pools (Gauge / Sparklines)
    3.  `nautobot.data_derived.vlan.utilization_by_site.percentage.avg` - VLAN Utilization by Site (Bar Chart)
    4.  `nautobot.data_derived.circuits.capacity_utilization.percentage.avg` (by provider/type) - Circuit Capacity Utilization (Time Series / Table)
    5.  `nautobot.data_derived.devices.by_status_and_role.count` - Device Count by Status and Role (Stacked Bar Chart)
    6.  Number of Single Points of Failure (derived from topology data, e.g., single-homed devices) (Big Number)
    7.  Data Completeness for Critical Service Attributes (e.g., % of devices with primary IP) (Gauge)

---

## 6.16 "Time to Value" Dashboard

*   **Purpose/Focus:** To measure how quickly Nautobot and its automation capabilities enable the delivery of new services or implementation of changes, highlighting agility.
*   **Target Audience:** IT Management, Business Stakeholders, Automation Program Leads.
*   **Key Metrics & Visualizations (Examples):**
    1.  `nautobot.business_impact.service_delivery.new_service.time_to_deploy.days.avg` - Avg. Time to Deploy New Service (end-to-end) (Time Series Line Chart)
    2.  `nautobot.business_impact.change_management.standard_change.implementation_time.hours.avg` - Avg. Time for Standard Change Implementation (Time Series Line Chart)
    3.  `nautobot.plugin_dlm.provisioning.device.time_to_active.seconds.avg` (Trend over time) - Device Provisioning Speed Trend (Line Chart)
    4.  `nautobot.roi.efficiency_gains.task_automation.speed_increase.percentage` (for specific automated tasks) - Task Speed Increase % (Bar Chart)
    5.  Cycle Time for Common Requests (e.g., New VLAN, Firewall Rule) (Histogram / Box Plot)
    6.  Number of Services/Changes Deployed via Automation vs. Manual (Monthly) (Stacked Bar Chart)
    7.  Lead Time from Request to Fulfillment for key services (Time Series)

---

## 6.17 "Error Reduction & Quality Improvement" Dashboard

*   **Purpose/Focus:** To track the impact of Nautobot and automation on reducing manual errors, improving change success rates, and enhancing overall operational quality.
*   **Target Audience:** IT Management, Operations Managers, Quality Assurance Teams.
*   **Key Metrics & Visualizations (Examples):**
    1.  `nautobot.roi.efficiency_gains.manual_error_reduction.percentage` - Reduction in Manual Error Rate (Time Series Line Chart)
    2.  `nautobot.value_driver.change_management.failure_rate.percentage` (overall, and for Nautobot-driven changes) - Change Failure Rate (Time Series Line Chart, compare manual vs automated)
    3.  `nautobot.plugin_golden_config.compliance.drift.detected.count` (Trend over time) - Compliance Drift Incidents (Time Series Line Chart)
    4.  `nautobot.business_impact.incident_resolution.mttr_reduction_from_automation.hours` - MTTR Reduction from Automation (Time Series Line Chart)
    5.  Number of Rollbacks/Hotfixes Required (Manual vs. Automated Changes) (Bar Chart)
    6.  `nautobot.plugin_ssot.discrepancy.detected.count` (Trend over time) - Data Discrepancies Over Time (Line Chart, indicating improved data quality)
    7.  Cost of Errors (e.g., `nautobot.roi.cost_avoidance.error_remediation.dollars.sum`) (Time Series Bar Chart)

---

## 6.18 Plugin Ecosystem Overview Dashboard

*   **Purpose/Focus:** To provide insights into the usage and activity levels of all installed Nautobot plugins, helping to identify popular, underutilized, or problematic plugins.
*   **Target Audience:** Platform Admins, Nautobot Developers, IT Management.
*   **Key Metrics & Visualizations (Examples):**
    1.  `nautobot.plugin_generic.usage.active_users.count` (by plugin_name) - Active Users per Plugin (Bar Chart)
    2.  `nautobot.plugin_generic.job_execution.total.count` (by plugin_name) - Job Executions per Plugin (Bar Chart / Treemap)
    3.  `nautobot.plugin_generic.feature_view.frequency.count` (by plugin_name, feature_name) - Page/Feature Views per Plugin (Table / Heatmap)
    4.  `nautobot.plugin_generic.object_management.creations_by_plugin.count` (by plugin_name, object_type) - Objects Created by Plugin (Stacked Bar Chart)
    5.  `nautobot.plugin_generic.job_execution.status.rate` (by plugin_name, status:failure) - Job Failure Rate per Plugin (Bar Chart)
    6.  `nautobot.plugin_generic.api_usage.request.count` (if plugin exposes dedicated API endpoints) - API Calls per Plugin (Time Series)
    7.  Last Activity Date per Plugin (Table)

---

## 6.19 "What-If" Scenario Planning Dashboard (Conceptual)

*   **Purpose/Focus:** To leverage historical Nautobot data and trends to model potential impacts of future changes or growth, aiding in capacity planning and resource allocation. (Note: This is more advanced and may require external data processing).
*   **Target Audience:** Network Planners, Capacity Management, IT Strategists.
*   **Key Metrics & Visualizations (Examples):**
    1.  Projected IP Address Utilization based on current growth rate (Time Series Forecast)
    2.  Impact of X% Device Growth on `nautobot.plugin_dlm.provisioning.device.time_to_active.seconds.avg` (Line Chart with projection)
    3.  Predicted Celery Worker Saturation based on job volume trends (Time Series Forecast)
    4.  Estimated Time to Reach Circuit Capacity Thresholds (Table with projections)
    5.  Correlation between New Sites Deployed and GC Job Execution Times (Scatter Plot with Trend Line)
    6.  Simulated impact of new SSoT source on data growth and sync times (Input fields + Chart output)
    7.  Forecasted need for additional Nautobot server resources based on user/API load growth (Line Chart)

---

## 6.20 Security & Audit Log Activity Dashboard

*   **Purpose/Focus:** To provide a focused view on security-relevant events and audit trails within Nautobot, aiding in security monitoring and compliance reporting.
*   **Target Audience:** Security Team, Audit Team, Platform Admins.
*   **Key Metrics & Visualizations (Examples):**
    1.  `nautobot.user_activity.authentication.login.failed.count` (Trend, Top Users with failures) (Time Series Line Chart, Table)
    2.  `nautobot.user_activity.authentication.login.success.from_suspicious_ip.count` (if IP intelligence is available) (Map / Table)
    3.  `nautobot.user_activity.object_management.critical_object.update.count` (e.g., global settings, user permissions) (Time Series Bar Chart / Table of changes)
    4.  `nautobot.user_activity.object_management.critical_object.delete.count` (Time Series Bar Chart / Table of changes)
    5.  `nautobot.user_activity.feature_usage.export.all_objects.count` (by user) - Full Data Export Activity (Bar Chart)
    6.  API Token Activity (Creations, Deletions, Last Used - if available) (Table)
    7.  `nautobot.user_activity.permissions.change.count` - User/Group Permission Changes (Time Series Bar Chart)

---

# High-Level Dashboard Implementation Guides

This section provides high-level, tool-agnostic implementation guides for each of the 20 conceptual dashboards previously defined. These guides are intended to assist in the creation of these dashboards using typical monitoring and visualization platforms (e.g., Grafana with Prometheus, ELK Stack, etc.).

---

## 7.1 Executive ROI & Business Value Dashboard

*   **Objective Reminder:** To provide a high-level overview of the tangible financial and operational benefits derived from implementing and utilizing Nautobot, focusing on cost savings, efficiency gains, and overall business value.
*   **Assumed Data Sources:** Metrics database (e.g., Prometheus, InfluxDB) storing Nautobot metrics, potentially financial tracking systems for cost inputs (manual or integrated).
*   **Key Panels/Visualizations - Step-by-Step:**
    1.  **Panel Title/Description:** Total Operational Cost Reduction (YTD)
        *   **Metric(s) to Use:** `nautobot.roi.cost_savings.operational.reduction.dollars.total` (sum over Year-to-Date)
        *   **Suggested Visualization Type:** Single Stat / Big Number
        *   **Brief Configuration Notes:** Sum the metric over the selected period (YTD). Optionally, show a comparison percentage to the previous year or a target.
    2.  **Panel Title/Description:** Total Hours Saved via Automation (YTD)
        *   **Metric(s) to Use:** `nautobot.roi.efficiency_gains.task_automation.time_saved.hours.sum` (sum over Year-to-Date)
        *   **Suggested Visualization Type:** Single Stat / Big Number
        *   **Brief Configuration Notes:** Sum the metric over the selected period (YTD). Display with a clear unit (e.g., "Hours Saved").
    3.  **Panel Title/Description:** Annualized Tooling Cost Savings
        *   **Metric(s) to Use:** `nautobot.roi.cost_savings.tool_consolidation.dollars.annual` (current value)
        *   **Suggested Visualization Type:** Gauge / Single Stat
        *   **Brief Configuration Notes:** Display the latest reported value for annualized savings. Set target if applicable.
    4.  **Panel Title/Description:** Overall Automation Adoption Rate
        *   **Metric(s) to Use:** `nautobot.roi.efficiency_gains.automation_adoption.percentage`
        *   **Suggested Visualization Type:** Gauge
        *   **Brief Configuration Notes:** Display the latest value. Set thresholds for green (>75%), yellow (50-75%), red (<50%).
    5.  **Panel Title/Description:** Trend of Operational Cost Reduction
        *   **Metric(s) to Use:** `nautobot.roi.cost_savings.operational.reduction.dollars.total`
        *   **Suggested Visualization Type:** Time Series Line Chart / Bar Chart
        *   **Brief Configuration Notes:** Plot monthly or quarterly sums. Compare against targets or previous periods if data is available.

*   **General Layout & Interactivity Suggestions:**
    *   Top row: Prominent display of the key single stat panels (Total Cost Reduction, Total Hours Saved, Tooling Savings, Adoption Rate).
    *   Main area: Trend charts for cost reduction and hours saved over time.
    *   Filters: Dashboard-level time range selector (e.g., "Last Quarter", "Last Year", "Year-to-Date").

---

## 7.2 Automation Program Health Dashboard

*   **Objective Reminder:** To monitor the overall health, adoption, and success of key automation initiatives powered by Nautobot, including Golden Configuration, SSoT, and DLM.
*   **Assumed Data Sources:** Metrics database (Prometheus/Grafana), Nautobot Job Result database, plugin-specific metrics.
*   **Key Panels/Visualizations - Step-by-Step:**
    1.  **Panel Title/Description:** Overall Automation Adoption Rate
        *   **Metric(s) to Use:** `nautobot.roi.efficiency_gains.automation_adoption.percentage`
        *   **Suggested Visualization Type:** Gauge / Time Series Line Chart
        *   **Brief Configuration Notes:** Gauge for current status, line chart for trend over time (e.g., last 90 days).
    2.  **Panel Title/Description:** Golden Configuration Overall Compliance
        *   **Metric(s) to Use:** `nautobot.plugin_golden_config.compliance.overall.percentage`
        *   **Suggested Visualization Type:** Gauge / Time Series Line Chart
        *   **Brief Configuration Notes:** Display latest compliance percentage. Show trend over time (e.g., last 30 days). Thresholds for acceptable compliance levels.
    3.  **Panel Title/Description:** SSoT Job Success Rate (by Source System)
        *   **Metric(s) to Use:** `nautobot.plugin_ssot.synchronization.job_status.rate` (query for success, group by `source_system` tag)
        *   **Suggested Visualization Type:** Bar Chart / Table
        *   **Brief Configuration Notes:** Calculate success rate: (successful jobs / total jobs) * 100 for each source system. Display over the last 7 or 30 days.
    4.  **Panel Title/Description:** DLM Automation Rate per Stage
        *   **Metric(s) to Use:** `nautobot.plugin_dlm.stage.automation.rate` (group by `stage_name` tag)
        *   **Suggested Visualization Type:** Bar Chart
        *   **Brief Configuration Notes:** Show the percentage of automation for each defined lifecycle stage.
    5.  **Panel Title/Description:** Overall Job Success Rate (All Jobs)
        *   **Metric(s) to Use:** `nautobot.job_execution.generic.status.rate` (query for success)
        *   **Suggested Visualization Type:** Time Series Line Chart / Gauge
        *   **Brief Configuration Notes:** Calculate overall success rate: (successful jobs / total jobs) * 100. Plot daily or weekly trend.

*   **General Layout & Interactivity Suggestions:**
    *   Top row: Key gauges for overall adoption and compliance.
    *   Main area: Bar charts for SSoT and DLM specifics, trend line for overall job success.
    *   Filters: Time range selector, filter by specific plugin (e.g., Golden Config, SSoT, DLM), filter by job trigger type (automated vs. manual).

---

## 7.3 Risk & Compliance Overview Dashboard

*   **Objective Reminder:** To provide management with a consolidated view of the organization's risk posture and compliance status as managed and monitored by Nautobot.
*   **Assumed Data Sources:** Metrics database, Nautobot application logs, data from Golden Configuration and SSoT plugins.
*   **Key Panels/Visualizations - Step-by-Step:**
    1.  **Panel Title/Description:** Overall Device Compliance Rate (Golden Config)
        *   **Metric(s) to Use:** `nautobot.plugin_golden_config.compliance.overall.percentage`
        *   **Suggested Visualization Type:** Gauge / Trend Line
        *   **Brief Configuration Notes:** Display current compliance rate. Trend line for the last 30/90 days to show improvement or degradation.
    2.  **Panel Title/Description:** High Severity Compliance Drifts (Last 7 Days)
        *   **Metric(s) to Use:** `nautobot.plugin_golden_config.compliance.drift.detected.count` (filter/group by `severity:high` tag if available, or by specific critical rule types)
        *   **Suggested Visualization Type:** Big Number / Table
        *   **Brief Configuration Notes:** Count of high severity drifts. Table lists affected devices and drift details.
    3.  **Panel Title/Description:** Data Staleness for Critical SSoT Systems
        *   **Metric(s) to Use:** `nautobot.plugin_ssot.data.staleness.hours.avg` (filter by `source_system` tag for critical systems)
        *   **Suggested Visualization Type:** Bar Chart / Table
        *   **Brief Configuration Notes:** Show average or max data staleness for SSoT integrations deemed critical. Highlight systems exceeding staleness thresholds.
    4.  **Panel Title/Description:** Failed Login Attempts (Last 24 Hours)
        *   **Metric(s) to Use:** `nautobot.user_activity.authentication.login.failed.count` (sum over last 24 hours)
        *   **Suggested Visualization Type:** Big Number / Time Series Bar Chart
        *   **Brief Configuration Notes:** Display total failed logins. Time series shows peaks which might indicate attacks.
    5.  **Panel Title/Description:** Critical Object Change Audit (Last 7 Days)
        *   **Metric(s) to Use:** `nautobot.user_activity.object_management.object.update.count` and `nautobot.user_activity.object_management.object.delete.count` (filter by tags identifying critical objects, e.g., `object_criticality:high`, or specific object types like `global_settings`)
        *   **Suggested Visualization Type:** Table / Event List
        *   **Brief Configuration Notes:** List critical object changes, including user, timestamp, and change details (if available from logs/events).

*   **General Layout & Interactivity Suggestions:**
    *   Top row: Key risk indicators (Compliance Rate, High Severity Drifts, Failed Logins).
    *   Main area: Charts for data staleness, trends in compliance. Audit log table for critical changes.
    *   Filters: Time range selector, filter by compliance rule severity, filter by SSoT source system.

---

## 7.4 Nautobot Platform Health & Usage Dashboard

*   **Objective Reminder:** To monitor the overall health, performance, and usage patterns of the Nautobot platform itself.
*   **Assumed Data Sources:** Metrics database (Prometheus/Grafana), Nautobot application logs, web server logs, Celery monitoring.
*   **Key Panels/Visualizations - Step-by-Step:**
    1.  **Panel Title/Description:** API Request Rate (RPM)
        *   **Metric(s) to Use:** `nautobot.system_performance.api.request.total.count`
        *   **Suggested Visualization Type:** Time Series Line Chart
        *   **Brief Configuration Notes:** Calculate rate per minute (e.g., `rate(metric[1m])` or `increase(metric[1m])`). Group by HTTP method or API endpoint for more detail.
    2.  **Panel Title/Description:** API Error Rate (P95 Latency & 5xx Errors)
        *   **Metric(s) to Use:** `nautobot.system_performance.api.response_time.seconds.p95`, `nautobot.system_performance.api.request.status_5xx.count`
        *   **Suggested Visualization Type:** Time Series Line Chart (for P95 latency), Time Series Bar Chart (for 5xx error count/rate)
        *   **Brief Configuration Notes:** Plot P95 latency. Calculate the rate of 5xx errors. Set alert thresholds for high latency or error rates.
    3.  **Panel Title/Description:** Active User Sessions
        *   **Metric(s) to Use:** `nautobot.user_activity.session_management.active_sessions.gauge`
        *   **Suggested Visualization Type:** Time Series Line Chart / Gauge
        *   **Brief Configuration Notes:** Display current active sessions and trend over time.
    4.  **Panel Title/Description:** Celery Task Queue Length
        *   **Metric(s) to Use:** `nautobot.system_performance.celery_workers.task_queue_length.gauge`
        *   **Suggested Visualization Type:** Time Series Line Chart (stacked by queue name if multiple queues)
        *   **Brief Configuration Notes:** Monitor queue lengths for backlogs. Alert if queues grow excessively.
    5.  **Panel Title/Description:** Top 10 Most Viewed Pages
        *   **Metric(s) to Use:** `nautobot.user_activity.feature_usage.page_view.frequency.count` (or similar from web server logs)
        *   **Suggested Visualization Type:** Bar Chart / Table
        *   **Brief Configuration Notes:** Aggregate page view counts over the selected time range and display the top 10.

*   **General Layout & Interactivity Suggestions:**
    *   Top row: KPIs for API health (request rate, error rate, P95 latency), Active Sessions.
    *   Main area: Time series charts for trends, tables for top lists.
    *   Filters: Time range selector, filter by API endpoint, filter by Celery queue name.

---

## 7.5 User Activity & Engagement Dashboard

*   **Objective Reminder:** To provide detailed insights into how users are interacting with Nautobot, which features they use, and overall engagement levels.
*   **Assumed Data Sources:** Metrics database, Nautobot application logs (tracking user actions, page views, feature usage).
*   **Key Panels/Visualizations - Step-by-Step:**
    1.  **Panel Title/Description:** Daily/Weekly Active Users (DAU/WAU)
        *   **Metric(s) to Use:** `nautobot.user_activity.authentication.login.success.count` (unique count of users)
        *   **Suggested Visualization Type:** Time Series Bar Chart / Line Chart
        *   **Brief Configuration Notes:** Aggregate unique users logging in daily and weekly.
    2.  **Panel Title/Description:** Average Session Duration
        *   **Metric(s) to Use:** `nautobot.user_activity.session_management.session_duration.seconds.avg`
        *   **Suggested Visualization Type:** Time Series Line Chart / Single Stat
        *   **Brief Configuration Notes:** Plot average session duration over time.
    3.  **Panel Title/Description:** Object Creations & Updates by Type
        *   **Metric(s) to Use:** `nautobot.user_activity.object_management.object.creation.count`, `nautobot.user_activity.object_management.object.update.count` (group by `object_type` tag)
        *   **Suggested Visualization Type:** Stacked Bar Chart (over time) or Pie Chart (current period)
        *   **Brief Configuration Notes:** Show trends in how different object types are being created or modified.
    4.  **Panel Title/Description:** Top Used Filters
        *   **Metric(s) to Use:** `nautobot.user_activity.feature_usage.filter_usage.frequency.count` (group by `filter_field` or `object_type` tag)
        *   **Suggested Visualization Type:** Bar Chart / Table
        *   **Brief Configuration Notes:** Display the most frequently used filter fields or filter patterns.
    5.  **Panel Title/Description:** Job Executions by User Group
        *   **Metric(s) to Use:** `nautobot.job_execution.generic.total.count` (group by `user_group` tag, filter by `trigger:manual` if desired)
        *   **Suggested Visualization Type:** Pie Chart / Bar Chart
        *   **Brief Configuration Notes:** Show which user groups are running the most jobs.

*   **General Layout & Interactivity Suggestions:**
    *   Top row: KPIs for DAU/WAU, Avg Session Duration.
    *   Main area: Charts for object CRUD activity, feature usage like filters and job executions.
    *   Filters: Time range selector, filter by user group, filter by object type.

---

## 7.6 Golden Configuration - Compliance Deep Dive

*   **Objective Reminder:** To provide a detailed view of device configuration compliance, enabling engineers to identify non-compliant devices, understand drift patterns, and track remediation progress.
*   **Assumed Data Sources:** Metrics database, Golden Configuration plugin database/metrics.
*   **Key Panels/Visualizations - Step-by-Step:**
    1.  **Panel Title/Description:** Overall Compliance Percentage
        *   **Metric(s) to Use:** `nautobot.plugin_golden_config.compliance.overall.percentage`
        *   **Suggested Visualization Type:** Gauge / Single Stat with Trend
        *   **Brief Configuration Notes:** Display current overall compliance. Show a small trend line for the last 7 days.
    2.  **Panel Title/Description:** Non-Compliant Devices List
        *   **Metric(s) to Use:** Query Golden Config data source for devices with `compliance_status: non-compliant`.
        *   **Suggested Visualization Type:** Table
        *   **Brief Configuration Notes:** Columns: Device Name, Site, Last Checked, Non-Compliant Rules, Severity. Allow sorting and filtering.
    3.  **Panel Title/Description:** Compliance Drift Trends (by Severity)
        *   **Metric(s) to Use:** `nautobot.plugin_golden_config.compliance.drift.detected.count` (group by `severity` tag if available, or `rule_type`)
        *   **Suggested Visualization Type:** Time Series Stacked Bar Chart / Line Chart
        *   **Brief Configuration Notes:** Plot daily/weekly count of new drifts, stacked by severity or rule type.
    4.  **Panel Title/Description:** Top Reasons for Non-Compliance
        *   **Metric(s) to Use:** `nautobot.plugin_golden_config.noncompliance.reason.top_reasons.count` (or parse from drift details)
        *   **Suggested Visualization Type:** Bar Chart
        *   **Brief Configuration Notes:** Show the most common configuration items or rule categories causing non-compliance.
    5.  **Panel Title/Description:** Automated Remediation Success Rate
        *   **Metric(s) to Use:** `nautobot.plugin_golden_config.remediation.automated.success.rate`
        *   **Suggested Visualization Type:** Gauge / Time Series Line Chart
        *   **Brief Configuration Notes:** Display overall success rate of automated remediations. Trend over time.

*   **General Layout & Interactivity Suggestions:**
    *   Top row: Overall Compliance Gauge, count of Non-Compliant Devices.
    *   Main area: Table of non-compliant devices, trend charts for drift, bar chart for non-compliance reasons.
    *   Filters: Time range selector, filter by device name/site, filter by compliance rule, filter by severity. Click on a non-compliant device in the table to see its detailed compliance report (if possible via linking).

---

## 7.7 Golden Configuration - Operational Dashboard

*   **Objective Reminder:** To monitor the operational aspects of the Golden Configuration plugin, including backup status, job performance, and common issues.
*   **Assumed Data Sources:** Metrics database, Golden Configuration plugin job logs/metrics.
*   **Key Panels/Visualizations - Step-by-Step:**
    1.  **Panel Title/Description:** Configuration Backup Status (Last 24h)
        *   **Metric(s) to Use:** `nautobot.plugin_golden_config.job.backup.status.rate` (count successful vs. failed)
        *   **Suggested Visualization Type:** Pie Chart / Bar Chart
        *   **Brief Configuration Notes:** Show the proportion of successful vs. failed backup jobs in the last 24 hours.
    2.  **Panel Title/Description:** Compliance Check Job Success Rate (Last 7d)
        *   **Metric(s) to Use:** `nautobot.plugin_golden_config.job.compliance_check.status.rate`
        *   **Suggested Visualization Type:** Time Series Line Chart (percentage) / Stacked Bar (count success vs. fail)
        *   **Brief Configuration Notes:** Track the daily success rate of compliance check jobs.
    3.  **Panel Title/Description:** Average Remediation Job Duration
        *   **Metric(s) to Use:** `nautobot.plugin_golden_config.job.remediation.duration.seconds.avg`
        *   **Suggested Visualization Type:** Time Series Line Chart
        *   **Brief Configuration Notes:** Plot the average duration of remediation jobs over time.
    4.  **Panel Title/Description:** Top Failing Backup/Compliance Jobs (Last 7d)
        *   **Metric(s) to Use:** Query GC job logs for failed jobs.
        *   **Suggested Visualization Type:** Table
        *   **Brief Configuration Notes:** Columns: Job ID, Device Name (if applicable), Error Message, Timestamp.
    5.  **Panel Title/Description:** GC Job Volume Trends (Backup, Compliance, Remediation)
        *   **Metric(s) to Use:** `nautobot.plugin_golden_config.job.execution.total.count` (group by job type: backup, compliance_check, remediation)
        *   **Suggested Visualization Type:** Time Series Stacked Bar Chart
        *   **Brief Configuration Notes:** Show daily/weekly volume of different GC job types.

*   **General Layout & Interactivity Suggestions:**
    *   Top row: KPIs for backup and compliance job success rates.
    *   Main area: Trend charts for job durations and volumes, table for failing jobs.
    *   Filters: Time range selector, filter by job type (backup, compliance, remediation), filter by device.

---

## 7.8 SSoT - Data Reconciliation & Integrity Dashboard

*   **Objective Reminder:** To monitor the health and effectiveness of Single Source of Truth (SSoT) integrations, focusing on data synchronization status, discrepancies, and data staleness.
*   **Assumed Data Sources:** Metrics database, SSoT plugin job logs/metrics, Nautobot change logs.
*   **Key Panels/Visualizations - Step-by-Step:**
    1.  **Panel Title/Description:** SSoT Job Success Rate (by Source System)
        *   **Metric(s) to Use:** `nautobot.plugin_ssot.synchronization.job.status.rate` (calculate success percentage, group by `source_system` tag)
        *   **Suggested Visualization Type:** Bar Chart / Table
        *   **Brief Configuration Notes:** Display success rate for each SSoT source over the last 7/30 days. Color-code by threshold (e.g., <90% red).
    2.  **Panel Title/Description:** Average SSoT Job Duration (by Source System)
        *   **Metric(s) to Use:** `nautobot.plugin_ssot.synchronization.job.duration.seconds.avg` (group by `source_system` tag)
        *   **Suggested Visualization Type:** Time Series Line Chart / Bar Chart
        *   **Brief Configuration Notes:** Plot average job duration for each source. Identify trends or consistently slow jobs.
    3.  **Panel Title/Description:** Discrepancies Detected vs. Resolved (by Source)
        *   **Metric(s) to Use:** `nautobot.plugin_ssot.discrepancy.detected.count`, `nautobot.plugin_ssot.discrepancy.resolved_automated.count` (group by `source_system` tag)
        *   **Suggested Visualization Type:** Time Series Stacked Bar Chart or Grouped Bar Chart
        *   **Brief Configuration Notes:** For each source, show total discrepancies detected and how many were auto-resolved over time.
    4.  **Panel Title/Description:** Data Staleness for Critical Systems
        *   **Metric(s) to Use:** `nautobot.plugin_ssot.data.staleness.hours.gauge` (filter for critical `source_system` tags)
        *   **Suggested Visualization Type:** Gauge / Bar Chart
        *   **Brief Configuration Notes:** Display current data staleness for important SSoT sources. Alert if staleness exceeds defined SLA.
    5.  **Panel Title/Description:** Top SSoT Job Failures (Last 7 Days)
        *   **Metric(s) to Use:** Query SSoT job logs for failures.
        *   **Suggested Visualization Type:** Table
        *   **Brief Configuration Notes:** Columns: Job Name, Source System, Error Message, Timestamp, Link to Logs.

*   **General Layout & Interactivity Suggestions:**
    *   Top row: KPIs for overall SSoT job success rate, total discrepancies.
    *   Main area: Charts for job duration, discrepancies by source, data staleness. Table for recent failures.
    *   Filters: Time range selector, filter by SSoT source system, filter by object type.

---

## 7.9 SSoT - Impact Analysis Dashboard

*   **Objective Reminder:** To understand the impact of SSoT jobs on Nautobot's data, tracking objects created, updated, or deleted by various integrations.
*   **Assumed Data Sources:** Metrics database, SSoT plugin job logs, Nautobot change logs (with SSoT user/source attribution).
*   **Key Panels/Visualizations - Step-by-Step:**
    1.  **Panel Title/Description:** Objects Created by SSoT (by Source & Type)
        *   **Metric(s) to Use:** `nautobot.plugin_ssot.objects_changed.created.count` (group by `source_system` and `object_type` tags)
        *   **Suggested Visualization Type:** Time Series Stacked Bar Chart
        *   **Brief Configuration Notes:** Show daily/weekly count of new objects created, stacked by SSoT source or object type.
    2.  **Panel Title/Description:** Objects Updated by SSoT (by Source & Type)
        *   **Metric(s) to Use:** `nautobot.plugin_ssot.objects_changed.updated.count` (group by `source_system` and `object_type` tags)
        *   **Suggested Visualization Type:** Time Series Stacked Bar Chart
        *   **Brief Configuration Notes:** Show daily/weekly count of object updates, stacked by SSoT source or object type.
    3.  **Panel Title/Description:** Objects Deleted by SSoT (by Source & Type)
        *   **Metric(s) to Use:** `nautobot.plugin_ssot.objects_changed.deleted.count` (group by `source_system` and `object_type` tags)
        *   **Suggested Visualization Type:** Time Series Stacked Bar Chart
        *   **Brief Configuration Notes:** Show daily/weekly count of object deletions, stacked by SSoT source or object type.
    4.  **Panel Title/Description:** Net Data Change Volume by SSoT Source
        *   **Metric(s) to Use:** Sum of `created.count`, `updated.count`, `deleted.count` grouped by `source_system`.
        *   **Suggested Visualization Type:** Sankey Diagram / Chord Diagram (if supported) or Grouped Bar Chart
        *   **Brief Configuration Notes:** Illustrate the flow and volume of data changes originating from each SSoT source.
    5.  **Panel Title/Description:** Most Active SSoT Integrations (by Change Volume)
        *   **Metric(s) to Use:** Sum of all `objects_changed.*.count` metrics, grouped by `source_system`.
        *   **Suggested Visualization Type:** Bar Chart / Treemap
        *   **Brief Configuration Notes:** Rank SSoT integrations by the total number of data modifications they perform.

*   **General Layout & Interactivity Suggestions:**
    *   Focus on time-series views to show trends in data modification by SSoT jobs.
    *   Use clear legends for SSoT sources and object types.
    *   Filters: Time range selector, filter by SSoT source system, filter by object type, filter by action (created, updated, deleted).

---

## 7.10 Device Lifecycle Management (DLM) - Efficiency Dashboard

*   **Objective Reminder:** To measure the efficiency of device lifecycle processes, focusing on time taken for key stages and the level of automation achieved.
*   **Assumed Data Sources:** Metrics database, DLM plugin data/metrics, potentially ticketing system data for request initiation.
*   **Key Panels/Visualizations - Step-by-Step:**
    1.  **Panel Title/Description:** Average Time to Provision New Device
        *   **Metric(s) to Use:** `nautobot.plugin_dlm.provisioning.device.time_to_active.seconds.avg`
        *   **Suggested Visualization Type:** Time Series Line Chart / Gauge with Trend
        *   **Brief Configuration Notes:** Plot average time from 'planned' to 'active'. Show trend over weeks/months.
    2.  **Panel Title/Description:** Average Time Spent in Each Lifecycle Stage
        *   **Metric(s) to Use:** `nautobot.plugin_dlm.stage.duration.avg.days` (group by `stage_name` tag)
        *   **Suggested Visualization Type:** Bar Chart (stages on one axis, avg time on the other)
        *   **Brief Configuration Notes:** Highlight stages where devices spend the most time.
    3.  **Panel Title/Description:** Automation Rate per Lifecycle Stage
        *   **Metric(s) to Use:** `nautobot.plugin_dlm.stage.automation.rate` (group by `stage_name` tag)
        *   **Suggested Visualization Type:** Stacked Bar Chart (each bar is a stage, stacked segments for % automated vs. % manual)
        *   **Brief Configuration Notes:** Clearly show the proportion of automation in each key lifecycle stage.
    4.  **Panel Title/Description:** Throughput of Device Provisioning (Devices/Week)
        *   **Metric(s) to Use:** Count of devices moved to 'active' state per week (derived from DLM logs/events or `nautobot.plugin_dlm.transition.success.count` where `to_stage:active`)
        *   **Suggested Visualization Type:** Bar Chart
        *   **Brief Configuration Notes:** Track the number of devices successfully provisioned each week.
    5.  **Panel Title/Description:** Manual Touchpoints per Lifecycle Process
        *   **Metric(s) to Use:** This might be a more qualitative metric or derived from summing non-automated steps defined in DLM.
        *   **Suggested Visualization Type:** Table / Heatmap
        *   **Brief Configuration Notes:** List key lifecycle processes (e.g., New Site Turnup, Device RMA) and the number of manual steps involved.

*   **General Layout & Interactivity Suggestions:**
    *   Top row: KPIs for overall provisioning time, overall automation rate.
    *   Main area: Charts showing time spent in stages, automation per stage, throughput.
    *   Filters: Time range selector, filter by device type, filter by site/region.

---

## 7.11 DLM - Operational Status Dashboard

*   **Objective Reminder:** To provide an operational overview of the device lifecycle, including current inventory status by stage, transition errors, and upcoming scheduled activities.
*   **Assumed Data Sources:** Metrics database, DLM plugin data/metrics.
*   **Key Panels/Visualizations - Step-by-Step:**
    1.  **Panel Title/Description:** Devices per Lifecycle Stage
        *   **Metric(s) to Use:** `nautobot.plugin_dlm.inventory.devices_by_stage.gauge` (group by `stage_name` tag)
        *   **Suggested Visualization Type:** Pie Chart / Donut Chart / Bar Chart
        *   **Brief Configuration Notes:** Show current distribution of devices across all defined lifecycle stages.
    2.  **Panel Title/Description:** Errors During Lifecycle Transitions (Last 7 Days)
        *   **Metric(s) to Use:** `nautobot.plugin_dlm.transition.error.count` (group by `from_stage`, `to_stage`, or `error_type` tags)
        *   **Suggested Visualization Type:** Bar Chart / Table
        *   **Brief Configuration Notes:** Highlight transitions or error types that are most problematic.
    3.  **Panel Title/Description:** Devices Overdue for Next Lifecycle Stage
        *   **Metric(s) to Use:** Derived by comparing current date with expected transition date for devices in non-final stages.
        *   **Suggested Visualization Type:** Table
        *   **Brief Configuration Notes:** Columns: Device Name, Current Stage, Expected Transition Date, Days Overdue. Requires logic to calculate expected dates.
    4.  **Panel Title/Description:** Lifecycle Process Adherence Rate
        *   **Metric(s) to Use:** `nautobot.plugin_dlm.process.adherence.rate`
        *   **Suggested Visualization Type:** Gauge
        *   **Brief Configuration Notes:** Display current adherence rate. Set thresholds for acceptable levels.
    5.  **Panel Title/Description:** Successfully Completed Transitions (Last 7 Days)
        *   **Metric(s) to Use:** `nautobot.plugin_dlm.transition.success.count` (group by `from_stage` and `to_stage` tags)
        *   **Suggested Visualization Type:** Bar Chart / Sankey Diagram
        *   **Brief Configuration Notes:** Show the volume of successful transitions between stages.

*   **General Layout & Interactivity Suggestions:**
    *   Top row: Device distribution by stage, overall process adherence rate.
    *   Main area: Tables for overdue devices and transition errors, chart for successful transitions.
    *   Filters: Time range selector, filter by lifecycle stage, filter by device type.

---

## 7.12 Job Execution & Automation Performance Dashboard

*   **Objective Reminder:** To monitor the overall performance and reliability of all jobs and automations running within Nautobot.
*   **Assumed Data Sources:** Metrics database (Prometheus/Grafana), Nautobot Job Result database, Celery monitoring.
*   **Key Panels/Visualizations - Step-by-Step:**
    1.  **Panel Title/Description:** Overall Job Success Rate
        *   **Metric(s) to Use:** `nautobot.job_execution.generic.status.rate` (calculate success percentage: successful jobs / total jobs * 100)
        *   **Suggested Visualization Type:** Gauge / Time Series Line Chart
        *   **Brief Configuration Notes:** Display current overall success rate. Trend line for daily/weekly success rate.
    2.  **Panel Title/Description:** Average Job Execution Time (P95)
        *   **Metric(s) to Use:** `nautobot.job_execution.generic.duration.seconds.p95`
        *   **Suggested Visualization Type:** Time Series Line Chart
        *   **Brief Configuration Notes:** Plot the 95th percentile of job execution times. Helps identify performance degradation.
    3.  **Panel Title/Description:** Job Throughput (Jobs per Minute)
        *   **Metric(s) to Use:** `nautobot.job_execution.generic.throughput.per_minute.count`
        *   **Suggested Visualization Type:** Time Series Line Chart
        *   **Brief Configuration Notes:** Monitor the rate of job processing.
    4.  **Panel Title/Description:** Top 10 Longest Running Jobs
        *   **Metric(s) to Use:** `nautobot.job_execution.generic.duration.seconds.avg` (group by `job_name` or `job_class_path` tag)
        *   **Suggested Visualization Type:** Table
        *   **Brief Configuration Notes:** List jobs with the highest average execution time over the selected period. Columns: Job Name, Avg Duration, Run Count.
    5.  **Panel Title/Description:** Top 10 Most Frequently Failing Jobs
        *   **Metric(s) to Use:** `nautobot.job_execution.generic.status.rate` (count failures, group by `job_name` or `job_class_path` tag)
        *   **Suggested Visualization Type:** Table
        *   **Brief Configuration Notes:** List jobs with the highest number of failures. Columns: Job Name, Failure Count, Last Error Message (if available).

*   **General Layout & Interactivity Suggestions:**
    *   Top row: KPIs for overall success rate, P95 execution time, current throughput.
    *   Main area: Trend charts for success rate and execution times. Tables for problematic jobs.
    *   Filters: Time range selector, filter by plugin name, filter by job name/class path, filter by job trigger (manual, scheduled, webhook).

---

## 7.13 Ansible Automation (via Nautobot) Performance

*   **Objective Reminder:** To specifically track the performance and outcomes of Ansible automation jobs that are integrated with or triggered by Nautobot.
*   **Assumed Data Sources:** Metrics database, Nautobot Job Result database (filtered for Ansible jobs), Ansible callback metrics (if configured).
*   **Key Panels/Visualizations - Step-by-Step:**
    1.  **Panel Title/Description:** Ansible Playbook Success Rate (from Nautobot)
        *   **Metric(s) to Use:** `nautobot.job_execution.generic.status.rate` (filtered by `job_type:ansible` or specific Ansible job name patterns, calculate success %)
        *   **Suggested Visualization Type:** Gauge / Time Series Line Chart (grouped by playbook name tag if available)
        *   **Brief Configuration Notes:** Track success rate of Ansible playbooks launched via Nautobot.
    2.  **Panel Title/Description:** Average Ansible Playbook Duration (from Nautobot)
        *   **Metric(s) to Use:** `nautobot.job_execution.generic.duration.seconds.avg` (filtered for Ansible jobs, grouped by playbook name tag)
        *   **Suggested Visualization Type:** Time Series Line Chart / Bar Chart
        *   **Brief Configuration Notes:** Monitor average execution time for different Ansible playbooks.
    3.  **Panel Title/Description:** Number of Configuration Changes by Ansible
        *   **Metric(s) to Use:** `nautobot.job_execution.ansible.changes_made.count` (if custom metric from Ansible callback) or derive from job logs/output.
        *   **Suggested Visualization Type:** Time Series Bar Chart
        *   **Brief Configuration Notes:** Track the volume of changes (tasks with `changed=true` status) made by Ansible.
    4.  **Panel Title/Description:** Top Failed Ansible Tasks (from Nautobot Jobs)
        *   **Metric(s) to Use:** Parse from Ansible job output/logs stored in Nautobot Job Results.
        *   **Suggested Visualization Type:** Table
        *   **Brief Configuration Notes:** Columns: Playbook Name, Task Name, Error Message, Host(s) Affected, Count. Requires parsing capabilities.
    5.  **Panel Title/Description:** Ansible Job Volume (from Nautobot)
        *   **Metric(s) to Use:** `nautobot.job_execution.generic.total.count` (filtered for Ansible jobs)
        *   **Suggested Visualization Type:** Time Series Bar Chart
        *   **Brief Configuration Notes:** Show the trend of Ansible job executions over time.

*   **General Layout & Interactivity Suggestions:**
    *   Top row: KPIs for overall Ansible playbook success rate, total changes made.
    *   Main area: Trend charts for durations and job volumes. Table for failed tasks.
    *   Filters: Time range selector, filter by Ansible playbook name, filter by target device/group (if tagged in job).

---

## 7.14 CI/CD Pipeline Integration Dashboard

*   **Objective Reminder:** To monitor the interaction and impact of Nautobot on CI/CD pipelines, especially where Nautobot data drives pipeline actions.
*   **Assumed Data Sources:** Metrics database, CI/CD system logs/APIs (e.g., Jenkins, GitLab CI), Nautobot event logs (if triggering pipelines).
*   **Key Panels/Visualizations - Step-by-Step:**
    1.  **Panel Title/Description:** CI/CD Pipelines Triggered by Nautobot Events
        *   **Metric(s) to Use:** `nautobot.integration.cicd.pipeline_trigger.from_nautobot_event.count` (or count from CI/CD system filtered by trigger source)
        *   **Suggested Visualization Type:** Time Series Bar Chart
        *   **Brief Configuration Notes:** Track how often Nautobot changes (e.g., webhook) initiate CI/CD pipelines.
    2.  **Panel Title/Description:** Pipeline Data Validation Success Rate (Nautobot Data)
        *   **Metric(s) to Use:** `nautobot.integration.cicd.data_validation.success.rate` (metric from CI/CD pipeline: success/failure of steps validating Nautobot data)
        *   **Suggested Visualization Type:** Gauge / Time Series Line Chart
        *   **Brief Configuration Notes:** Monitor reliability of data consumed from Nautobot by CI/CD.
    3.  **Panel Title/Description:** Avg. Deployment Time (Nautobot-driven Pipelines)
        *   **Metric(s) to Use:** `nautobot.integration.cicd.deployment.using_nautobot_data.duration.seconds.avg` (metric from CI/CD system for relevant pipelines)
        *   **Suggested Visualization Type:** Time Series Line Chart
        *   **Brief Configuration Notes:** Track deployment duration for pipelines that depend on Nautobot.
    4.  **Panel Title/Description:** Failure Rate of Deployments Using Nautobot Data
        *   **Metric(s) to Use:** `nautobot.integration.cicd.deployment.using_nautobot_data.failure.rate` (metric from CI/CD system)
        *   **Suggested Visualization Type:** Gauge / Time Series Line Chart
        *   **Brief Configuration Notes:** Highlight if changes sourced from Nautobot are leading to deployment failures.
    5.  **Panel Title/Description:** Types of CI/CD Jobs Utilizing Nautobot Data
        *   **Metric(s) to Use:** Count of pipeline executions, grouped by job type/stage (e.g., pre-check, deploy, post-check) that use Nautobot data.
        *   **Suggested Visualization Type:** Pie Chart / Bar Chart
        *   **Brief Configuration Notes:** Understand which parts of the CI/CD process are most reliant on Nautobot.

*   **General Layout & Interactivity Suggestions:**
    *   Top row: KPIs for pipeline trigger frequency, validation success rate, deployment failure rate.
    *   Main area: Trend charts for deployment times and pipeline activities.
    *   Filters: Time range selector, filter by CI/CD pipeline name/project, filter by Nautobot event type (if applicable).

---

## 7.15 Network Services Health (derived from Nautobot data)

*   **Objective Reminder:** To leverage Nautobot's SSoT data to provide insights into the health and utilization of key network services.
*   **Assumed Data Sources:** Metrics database (data populated by a process that regularly queries Nautobot API for relevant data points and exposes them as metrics).
*   **Key Panels/Visualizations - Step-by-Step:**
    1.  **Panel Title/Description:** Average IP Prefix Utilization (by VRF/Region)
        *   **Metric(s) to Use:** `nautobot.data_derived.ipam.prefix_utilization.percentage.avg` (tags: `vrf`, `region`)
        *   **Suggested Visualization Type:** Heatmap / Bar Chart / Table
        *   **Brief Configuration Notes:** Color-code by utilization thresholds (e.g., >80% red, >60% yellow).
    2.  **Panel Title/Description:** Available IP Addresses in Critical Pools
        *   **Metric(s) to Use:** `nautobot.data_derived.ipam.available_ips.count` (filter by tag `ip_pool_criticality:high`)
        *   **Suggested Visualization Type:** Gauge / Sparkline per pool / Table
        *   **Brief Configuration Notes:** Monitor free IPs in important address pools. Alert when low.
    3.  **Panel Title/Description:** VLAN Utilization by Site
        *   **Metric(s) to Use:** `nautobot.data_derived.vlan.utilization_by_site.percentage.avg` (tag: `site`)
        *   **Suggested Visualization Type:** Bar Chart / Table
        *   **Brief Configuration Notes:** Show average VLAN utilization per site, or top N utilized sites.
    4.  **Panel Title/Description:** Device Count by Status and Role
        *   **Metric(s) to Use:** `nautobot.data_derived.devices.by_status_and_role.count` (tags: `device_status`, `device_role`)
        *   **Suggested Visualization Type:** Stacked Bar Chart / Grouped Bar Chart
        *   **Brief Configuration Notes:** Provide an overview of the device inventory breakdown.
    5.  **Panel Title/Description:** Data Completeness for Critical Attributes
        *   **Metric(s) to Use:** E.g., percentage of 'active' devices that have 'primary_ip' populated, or 'serial_number' recorded.
        *   **Suggested Visualization Type:** Gauge / Bullet Chart
        *   **Brief Configuration Notes:** Requires a separate script/process to calculate these completeness metrics from Nautobot data and expose them.

*   **General Layout & Interactivity Suggestions:**
    *   Layout based on service areas (IPAM, VLANs, Devices, Circuits).
    *   Use gauges for at-a-glance status of critical resources.
    *   Filters: Filter by Site, Region, VRF, Device Role, Device Status.

---

## 7.16 "Time to Value" Dashboard

*   **Objective Reminder:** To measure how quickly Nautobot and its automation capabilities enable the delivery of new services or implementation of changes, highlighting agility.
*   **Target Audience:** IT Management, Business Stakeholders, Automation Program Leads.
*   **Key Panels/Visualizations - Step-by-Step:**
    1.  **Panel Title/Description:** Avg. Time to Deploy New Service (End-to-End)
        *   **Metric(s) to Use:** `nautobot.business_impact.service_delivery.new_service.time_to_deploy.days.avg`
        *   **Suggested Visualization Type:** Time Series Line Chart / Single Stat with Trend
        *   **Brief Configuration Notes:** Track this average over time (monthly/quarterly) to show improvements.
    2.  **Panel Title/Description:** Avg. Time for Standard Change Implementation
        *   **Metric(s) to Use:** `nautobot.business_impact.change_management.standard_change.implementation_time.hours.avg`
        *   **Suggested Visualization Type:** Time Series Line Chart
        *   **Brief Configuration Notes:** Focus on common, repeatable changes that have been automated.
    3.  **Panel Title/Description:** Device Provisioning Speed Trend (Time to Active)
        *   **Metric(s) to Use:** `nautobot.plugin_dlm.provisioning.device.time_to_active.seconds.avg`
        *   **Suggested Visualization Type:** Time Series Line Chart
        *   **Brief Configuration Notes:** Shows efficiency gains in the core device turn-up process.
    4.  **Panel Title/Description:** Task Speed Increase % (for Specific Automations)
        *   **Metric(s) to Use:** `nautobot.roi.efficiency_gains.task_automation.speed_increase.percentage` (filter by `task_name` tag)
        *   **Suggested Visualization Type:** Bar Chart
        *   **Brief Configuration Notes:** Highlight the percentage improvement for key automated tasks compared to previous manual methods.
    5.  **Panel Title/Description:** Cycle Time for Common Requests (e.g., New VLAN)
        *   **Metric(s) to Use:** Derived from start/end timestamps of jobs or workflows related to specific requests.
        *   **Suggested Visualization Type:** Histogram / Box Plot
        *   **Brief Configuration Notes:** Shows distribution of completion times for frequent, standardized requests.

*   **General Layout & Interactivity Suggestions:**
    *   Top row: KPIs for key "time to X" metrics.
    *   Main area: Trend lines showing improvements over time. Bar charts for comparisons.
    *   Filters: Time range selector, filter by service type, filter by change type, filter by automation task name.

---

## 7.17 "Error Reduction & Quality Improvement" Dashboard

*   **Objective Reminder:** To track the impact of Nautobot and automation on reducing manual errors, improving change success rates, and enhancing overall operational quality.
*   **Assumed Data Sources:** Metrics database, Nautobot Job Results, incident management system data, change management system data.
*   **Key Panels/Visualizations - Step-by-Step:**
    1.  **Panel Title/Description:** Reduction in Manual Error Rate %
        *   **Metric(s) to Use:** `nautobot.roi.efficiency_gains.manual_error_reduction.percentage`
        *   **Suggested Visualization Type:** Time Series Line Chart / Gauge
        *   **Brief Configuration Notes:** Plot the calculated reduction percentage over time.
    2.  **Panel Title/Description:** Change Failure Rate (Manual vs. Automated)
        *   **Metric(s) to Use:** `nautobot.value_driver.change_management.failure_rate.percentage` (use tags to distinguish `source:manual` vs. `source:automated_nautobot`)
        *   **Suggested Visualization Type:** Grouped Time Series Bar Chart or Line Chart
        *   **Brief Configuration Notes:** Compare failure rates of changes implemented manually versus those driven by Nautobot automation.
    3.  **Panel Title/Description:** Compliance Drift Incidents Trend
        *   **Metric(s) to Use:** `nautobot.plugin_golden_config.compliance.drift.detected.count`
        *   **Suggested Visualization Type:** Time Series Line Chart / Bar Chart
        *   **Brief Configuration Notes:** Track the number of new compliance drifts detected over time. A downward trend indicates improving quality.
    4.  **Panel Title/Description:** MTTR Reduction from Automation
        *   **Metric(s) to Use:** `nautobot.business_impact.incident_resolution.mttr_reduction_from_automation.hours`
        *   **Suggested Visualization Type:** Time Series Line Chart
        *   **Brief Configuration Notes:** Plot the difference in MTTR for incidents resolved with automation vs. purely manual efforts.
    5.  **Panel Title/Description:** Data Discrepancies Over Time (SSoT)
        *   **Metric(s) to Use:** `nautobot.plugin_ssot.discrepancy.detected.count`
        *   **Suggested Visualization Type:** Time Series Line Chart
        *   **Brief Configuration Notes:** A decreasing trend can indicate improved data quality and SSoT effectiveness.

*   **General Layout & Interactivity Suggestions:**
    *   Top row: KPIs for overall error reduction, change failure rate.
    *   Main area: Trend charts comparing manual vs. automated performance, trends for compliance drifts and data discrepancies.
    *   Filters: Time range selector, filter by change type, filter by automation area (e.g., Golden Config, SSoT).

---

## 7.18 Plugin Ecosystem Overview Dashboard

*   **Objective Reminder:** To provide insights into the usage and activity levels of all installed Nautobot plugins, helping to identify popular, underutilized, or problematic plugins.
*   **Assumed Data Sources:** Metrics database (with `plugin_name` tag on relevant metrics), Nautobot Job Results, application logs.
*   **Key Panels/Visualizations - Step-by-Step:**
    1.  **Panel Title/Description:** Active Users per Plugin (Last 30 Days)
        *   **Metric(s) to Use:** `nautobot.plugin_generic.usage.active_users.count` (group by `plugin_name` tag) or derive from page views/job executions tagged by plugin.
        *   **Suggested Visualization Type:** Bar Chart
        *   **Brief Configuration Notes:** Show unique user count interacting with features or jobs of each plugin.
    2.  **Panel Title/Description:** Job Executions per Plugin
        *   **Metric(s) to Use:** `nautobot.job_execution.generic.total.count` (group by `plugin_name` tag)
        *   **Suggested Visualization Type:** Bar Chart / Treemap
        *   **Brief Configuration Notes:** Display total job runs for each plugin over the selected time period.
    3.  **Panel Title/Description:** Page/Feature Views per Plugin
        *   **Metric(s) to Use:** `nautobot.user_activity.feature_usage.page_view.frequency.count` (group by `plugin_name` tag, then `feature_name` or `page_url`)
        *   **Suggested Visualization Type:** Table / Heatmap
        *   **Brief Configuration Notes:** Show most accessed UI components provided by each plugin.
    4.  **Panel Title/Description:** Job Failure Rate per Plugin
        *   **Metric(s) to Use:** `nautobot.job_execution.generic.status.rate` (calculate failure rate, group by `plugin_name` tag)
        *   **Suggested Visualization Type:** Bar Chart
        *   **Brief Configuration Notes:** Highlight plugins with higher job failure rates.
    5.  **Panel Title/Description:** Objects Created/Modified by Plugin
        *   **Metric(s) to Use:** `nautobot.user_activity.object_management.object.creation.count`, `nautobot.user_activity.object_management.object.update.count` (group by `source:plugin_name` tag or similar custom tag)
        *   **Suggested Visualization Type:** Stacked Bar Chart
        *   **Brief Configuration Notes:** Show which plugins are contributing most to data creation/modification.

*   **General Layout & Interactivity Suggestions:**
    *   Use a consistent color scheme for each plugin across different charts if possible.
    *   Allow drilling down from a plugin in one panel to see its specific metrics in other panels.
    *   Filters: Time range selector, select specific plugin_name to deep-dive.

---

## 7.19 "What-If" Scenario Planning Dashboard (Conceptual)

*   **Objective Reminder:** To leverage historical Nautobot data and trends to model potential impacts of future changes or growth, aiding in capacity planning and resource allocation. (Advanced: May require external data processing & forecasting tools).
*   **Assumed Data Sources:** Metrics database, external forecasting tools/scripts that can read from the metrics DB and write back projections.
*   **Key Panels/Visualizations - Step-by-Step:**
    1.  **Panel Title/Description:** Projected IP Address Utilization
        *   **Metric(s) to Use:** `nautobot.data_derived.ipam.prefix_utilization.percentage.avg` (historical data), plus a forecasted series.
        *   **Suggested Visualization Type:** Time Series Line Chart with Forecast Overlay
        *   **Brief Configuration Notes:** Plot historical utilization and overlay a projection (e.g., linear regression, ARIMA) for the next 6-12 months.
    2.  **Panel Title/Description:** Predicted Celery Worker Saturation
        *   **Metric(s) to Use:** `nautobot.job_execution.generic.throughput.per_minute.count` (historical), `nautobot.system_performance.celery_workers.utilization.percentage` (if available). Forecast job growth.
        *   **Suggested Visualization Type:** Time Series Line Chart with Forecast & Threshold
        *   **Brief Configuration Notes:** Project future job volumes and estimate when worker capacity might be breached.
    3.  **Panel Title/Description:** Impact of X% Device Growth on Provisioning Time
        *   **Metric(s) to Use:** `nautobot.plugin_dlm.provisioning.device.time_to_active.seconds.avg` (historical). Requires a model to correlate device count with provisioning time.
        *   **Suggested Visualization Type:** Line Chart with Input for Growth % and Projected Impact
        *   **Brief Configuration Notes:** User inputs a device growth percentage; dashboard shows potential impact on average provisioning time based on a simplified model.
    4.  **Panel Title/Description:** Estimated Time to Reach Circuit Capacity Thresholds
        *   **Metric(s) to Use:** `nautobot.data_derived.circuits.capacity_utilization.percentage.avg` (historical).
        *   **Suggested Visualization Type:** Table with Projected Dates
        *   **Brief Configuration Notes:** For key circuits, project current utilization trend to estimate when they might hit 80% or 90% capacity.

*   **General Layout & Interactivity Suggestions:**
    *   Clearly label historical vs. projected data.
    *   Provide input fields for users to tweak assumptions (e.g., growth rate).
    *   Include notes about the forecasting model's limitations.
    *   Filters: Time range for historical data, selectable forecast horizon.

---

## 7.20 Security & Audit Log Activity Dashboard

*   **Objective Reminder:** To provide a focused view on security-relevant events and audit trails within Nautobot, aiding in security monitoring and compliance reporting.
*   **Assumed Data Sources:** Metrics database, Nautobot application logs (especially authentication and audit logs), web server logs.
*   **Key Panels/Visualizations - Step-by-Step:**
    1.  **Panel Title/Description:** Failed Login Attempts Trend & Top Users
        *   **Metric(s) to Use:** `nautobot.user_activity.authentication.login.failed.count` (overall trend and grouped by `user_name` tag)
        *   **Suggested Visualization Type:** Time Series Line Chart (for trend), Table (for top users with failed attempts)
        *   **Brief Configuration Notes:** Monitor spikes in failed logins. Identify accounts being targeted.
    2.  **Panel Title/Description:** Critical Object Changes (Last 7 Days)
        *   **Metric(s) to Use:** `nautobot.user_activity.object_management.object.update.count`, `nautobot.user_activity.object_management.object.delete.count` (filter by tags: `object_criticality:high` or specific sensitive object types like `user`, `permission`, `gitrepository`).
        *   **Suggested Visualization Type:** Event List / Table
        *   **Brief Configuration Notes:** Detail who changed what critical object, and when.
    3.  **Panel Title/Description:** Full Data Export Activity
        *   **Metric(s) to Use:** `nautobot.user_activity.feature_usage.export.all_objects.count` (or similar if specific metric exists for full exports, group by `user_name`)
        *   **Suggested Visualization Type:** Bar Chart / Table
        *   **Brief Configuration Notes:** Track who is exporting large datasets and how often.
    4.  **Panel Title/Description:** User/Group Permission Changes
        *   **Metric(s) to Use:** `nautobot.user_activity.permissions.change.count` (group by `target_user` or `target_group`, and `action:granted/revoked`)
        *   **Suggested Visualization Type:** Time Series Bar Chart / Event List
        *   **Brief Configuration Notes:** Monitor changes to user and group permissions.
    5.  **Panel Title/Description:** API Token Activity (Last 30 Days)
        *   **Metric(s) to Use:** Metrics for API token creation, deletion, last used (if available, e.g., from audit logs).
        *   **Suggested Visualization Type:** Table
        *   **Brief Configuration Notes:** List recently created/deleted tokens, and tokens nearing expiry or unused for a long time.

*   **General Layout & Interactivity Suggestions:**
    *   Prioritize event lists and tables for detailed audit.
    *   Use clear timestamps and user attribution for all events.
    *   Filters: Time range selector, filter by user name, filter by object type (for changes), filter by event type (login, CRUD, permission change).

---

# Conclusion

This document has laid out a comprehensive framework for Nautobot metrics, encompassing core categories, specific metric definitions, standardized naming conventions, a suite of conceptual dashboard designs, and high-level implementation guidance. It serves as a blueprint for enhancing observability into Nautobot deployments, enabling data-driven decision-making, and showcasing the platform's value across various operational and strategic dimensions.

The next steps involve operationalizing this framework. This includes implementing the necessary metric collection mechanisms within Nautobot and its ecosystem, integrating with chosen monitoring and visualization platforms (such as Prometheus and Grafana), and progressively building out the proposed dashboards. Continuous refinement of these metrics and dashboards, based on evolving organizational needs and user feedback, will be crucial for ensuring their sustained relevance and maximizing the value derived from Nautobot monitoring.
