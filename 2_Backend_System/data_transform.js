/**
 * AGIcam Data Transformation Function
 * Author: Nisit Pukrongta and Worasit Sangjan
 * Date: April 2022
 */

// Multi-replicate data transformation
msg.payload = [
    // ============ REPLICATE 1 ============
    // Rep1_vr1_1
    {
        measurement: "vr1_1",
        fields: {
            timepi: msg.payload.rep1.vr1_1.timestamp,
            mean: msg.payload.rep1.vr1_1.mean,
            median: msg.payload.rep1.vr1_1.median,
            std: msg.payload.rep1.vr1_1.std,
            max: msg.payload.rep1.vr1_1.max,
            p95: msg.payload.rep1.vr1_1.p95,
            p90: msg.payload.rep1.vr1_1.p90,
            p85: msg.payload.rep1.vr1_1.p85
        },
        tags: {
            plot: "rep1"
        },
        timestamp: new Date()
    },
    
    // Rep1_vr2_1
    {
        measurement: "vr2_1",
        fields: {
            timepi: msg.payload.rep1.vr2_1.timestamp,
            mean: msg.payload.rep1.vr2_1.mean,
            median: msg.payload.rep1.vr2_1.median,
            std: msg.payload.rep1.vr2_1.std,
            max: msg.payload.rep1.vr2_1.max,
            p95: msg.payload.rep1.vr2_1.p95,
            p90: msg.payload.rep1.vr2_1.p90,
            p85: msg.payload.rep1.vr2_1.p85
        },
        tags: {
            plot: "rep1"
        },
        timestamp: new Date()
    },
    
    // Rep1_vr3_1
    {
        measurement: "vr3_1",
        fields: {
            timepi: msg.payload.rep1.vr3_1.timestamp,
            mean: msg.payload.rep1.vr3_1.mean,
            median: msg.payload.rep1.vr3_1.median,
            std: msg.payload.rep1.vr3_1.std,
            max: msg.payload.rep1.vr3_1.max,
            p95: msg.payload.rep1.vr3_1.p95,
            p90: msg.payload.rep1.vr3_1.p90,
            p85: msg.payload.rep1.vr3_1.p85
        },
        tags: {
            plot: "rep1"
        },
        timestamp: new Date()
    },
    
    // Rep1_vr4_1
    {
        measurement: "vr4_1",
        fields: {
            timepi: msg.payload.rep1.vr4_1.timestamp,
            mean: msg.payload.rep1.vr4_1.mean,
            median: msg.payload.rep1.vr4_1.median,
            std: msg.payload.rep1.vr4_1.std,
            max: msg.payload.rep1.vr4_1.max,
            p95: msg.payload.rep1.vr4_1.p95,
            p90: msg.payload.rep1.vr4_1.p90,
            p85: msg.payload.rep1.vr4_1.p85
        },
        tags: {
            plot: "rep1"
        },
        timestamp: new Date()
    },

    // ============ REPLICATE 2 ============
    // Rep2_vr1_1
    {
        measurement: "vr1_1",
        fields: {
            timepi: msg.payload.rep2.vr1_1.timestamp,
            mean: msg.payload.rep2.vr1_1.mean,
            median: msg.payload.rep2.vr1_1.median,
            std: msg.payload.rep2.vr1_1.std,
            max: msg.payload.rep2.vr1_1.max,
            p95: msg.payload.rep2.vr1_1.p95,
            p90: msg.payload.rep2.vr1_1.p90,
            p85: msg.payload.rep2.vr1_1.p85
        },
        tags: {
            plot: "rep2"
        },
        timestamp: new Date()
    },
    
    // Rep2_vr2_1
    {
        measurement: "vr2_1",
        fields: {
            timepi: msg.payload.rep2.vr2_1.timestamp,
            mean: msg.payload.rep2.vr2_1.mean,
            median: msg.payload.rep2.vr2_1.median,
            std: msg.payload.rep2.vr2_1.std,
            max: msg.payload.rep2.vr2_1.max,
            p95: msg.payload.rep2.vr2_1.p95,
            p90: msg.payload.rep2.vr2_1.p90,
            p85: msg.payload.rep2.vr2_1.p85
        },
        tags: {
            plot: "rep2"
        },
        timestamp: new Date()
    },
    
    // Rep2_vr3_1
    {
        measurement: "vr3_1",
        fields: {
            timepi: msg.payload.rep2.vr3_1.timestamp,
            mean: msg.payload.rep2.vr3_1.mean,
            median: msg.payload.rep2.vr3_1.median,
            std: msg.payload.rep2.vr3_1.std,
            max: msg.payload.rep2.vr3_1.max,
            p95: msg.payload.rep2.vr3_1.p95,
            p90: msg.payload.rep2.vr3_1.p90,
            p85: msg.payload.rep2.vr3_1.p85
        },
        tags: {
            plot: "rep2"
        },
        timestamp: new Date()
    },
    
    // Rep2_vr4_1
    {
        measurement: "vr4_1",
        fields: {
            timepi: msg.payload.rep2.vr4_1.timestamp,
            mean: msg.payload.rep2.vr4_1.mean,
            median: msg.payload.rep2.vr4_1.median,
            std: msg.payload.rep2.vr4_1.std,
            max: msg.payload.rep2.vr4_1.max,
            p95: msg.payload.rep2.vr4_1.p95,
            p90: msg.payload.rep2.vr4_1.p90,
            p85: msg.payload.rep2.vr4_1.p85
        },
        tags: {
            plot: "rep2"
        },
        timestamp: new Date()
    },

    // ============ REPLICATE 3 ============
    // Rep3_vr1_1
    {
        measurement: "vr1_1",
        fields: {
            timepi: msg.payload.rep3.vr1_1.timestamp,
            mean: msg.payload.rep3.vr1_1.mean,
            median: msg.payload.rep3.vr1_1.median,
            std: msg.payload.rep3.vr1_1.std,
            max: msg.payload.rep3.vr1_1.max,
            p95: msg.payload.rep3.vr1_1.p95,
            p90: msg.payload.rep3.vr1_1.p90,
            p85: msg.payload.rep3.vr1_1.p85
        },
        tags: {
            plot: "rep3"
        },
        timestamp: new Date()
    },
    
    // Rep3_vr2_1
    {
        measurement: "vr2_1",
        fields: {
            timepi: msg.payload.rep3.vr2_1.timestamp,
            mean: msg.payload.rep3.vr2_1.mean,
            median: msg.payload.rep3.vr2_1.median,
            std: msg.payload.rep3.vr2_1.std,
            max: msg.payload.rep3.vr2_1.max,
            p95: msg.payload.rep3.vr2_1.p95,
            p90: msg.payload.rep3.vr2_1.p90,
            p85: msg.payload.rep3.vr2_1.p85
        },
        tags: {
            plot: "rep3"
        },
        timestamp: new Date()
    },
    
    // Rep3_vr3_1
    {
        measurement: "vr3_1",
        fields: {
            timepi: msg.payload.rep3.vr3_1.timestamp,
            mean: msg.payload.rep3.vr3_1.mean,
            median: msg.payload.rep3.vr3_1.median,
            std: msg.payload.rep3.vr3_1.std,
            max: msg.payload.rep3.vr3_1.max,
            p95: msg.payload.rep3.vr3_1.p95,
            p90: msg.payload.rep3.vr3_1.p90,
            p85: msg.payload.rep3.vr3_1.p85
        },
        tags: {
            plot: "rep3"
        },
        timestamp: new Date()
    },
    
    // Rep3_vr4_1
    {
        measurement: "vr4_1",
        fields: {
            timepi: msg.payload.rep3.vr4_1.timestamp,
            mean: msg.payload.rep3.vr4_1.mean,
            median: msg.payload.rep3.vr4_1.median,
            std: msg.payload.rep3.vr4_1.std,
            max: msg.payload.rep3.vr4_1.max,
            p95: msg.payload.rep3.vr4_1.p95,
            p90: msg.payload.rep3.vr4_1.p90,
            p85: msg.payload.rep3.vr4_1.p85
        },
        tags: {
            plot: "rep3"
        },
        timestamp: new Date()
    },

    // ============ REPLICATE 4 ============
    // Rep4_vr1_1
    {
        measurement: "vr1_1",
        fields: {
            timepi: msg.payload.rep4.vr1_1.timestamp,
            mean: msg.payload.rep4.vr1_1.mean,
            median: msg.payload.rep4.vr1_1.median,
            std: msg.payload.rep4.vr1_1.std,
            max: msg.payload.rep4.vr1_1.max,
            p95: msg.payload.rep4.vr1_1.p95,
            p90: msg.payload.rep4.vr1_1.p90,
            p85: msg.payload.rep4.vr1_1.p85
        },
        tags: {
            plot: "rep4"
        },
        timestamp: new Date()
    },
    
    // Rep4_vr2_1
    {
        measurement: "vr2_1",
        fields: {
            timepi: msg.payload.rep4.vr2_1.timestamp,
            mean: msg.payload.rep4.vr2_1.mean,
            median: msg.payload.rep4.vr2_1.median,
            std: msg.payload.rep4.vr2_1.std,
            max: msg.payload.rep4.vr2_1.max,
            p95: msg.payload.rep4.vr2_1.p95,
            p90: msg.payload.rep4.vr2_1.p90,
            p85: msg.payload.rep4.vr2_1.p85
        },
        tags: {
            plot: "rep4"
        },
        timestamp: new Date()
    },
    
    // Rep4_vr3_1
    {
        measurement: "vr3_1",
        fields: {
            timepi: msg.payload.rep4.vr3_1.timestamp,
            mean: msg.payload.rep4.vr3_1.mean,
            median: msg.payload.rep4.vr3_1.median,
            std: msg.payload.rep4.vr3_1.std,
            max: msg.payload.rep4.vr3_1.max,
            p95: msg.payload.rep4.vr3_1.p95,
            p90: msg.payload.rep4.vr3_1.p90,
            p85: msg.payload.rep4.vr3_1.p85
        },
        tags: {
            plot: "rep4"
        },
        timestamp: new Date()
    },
    
    // Rep4_vr4_1
    {
        measurement: "vr4_1",
        fields: {
            timepi: msg.payload.rep4.vr4_1.timestamp,
            mean: msg.payload.rep4.vr4_1.mean,
            median: msg.payload.rep4.vr4_1.median,
            std: msg.payload.rep4.vr4_1.std,
            max: msg.payload.rep4.vr4_1.max,
            p95: msg.payload.rep4.vr4_1.p95,
            p90: msg.payload.rep4.vr4_1.p90,
            p85: msg.payload.rep4.vr4_1.p85
        },
        tags: {
            plot: "rep4"
        },
        timestamp: new Date()
    },

    // ============ REPLICATE 5 ============
    // Rep5_vr1_1
    {
        measurement: "vr1_1",
        fields: {
            timepi: msg.payload.rep5.vr1_1.timestamp,
            mean: msg.payload.rep5.vr1_1.mean,
            median: msg.payload.rep5.vr1_1.median,
            std: msg.payload.rep5.vr1_1.std,
            max: msg.payload.rep5.vr1_1.max,
            p95: msg.payload.rep5.vr1_1.p95,
            p90: msg.payload.rep5.vr1_1.p90,
            p85: msg.payload.rep5.vr1_1.p85
        },
        tags: {
            plot: "rep5"
        },
        timestamp: new Date()
    },
    
    // Rep5_vr2_1
    {
        measurement: "vr2_1",
        fields: {
            timepi: msg.payload.rep5.vr2_1.timestamp,
            mean: msg.payload.rep5.vr2_1.mean,
            median: msg.payload.rep5.vr2_1.median,
            std: msg.payload.rep5.vr2_1.std,
            max: msg.payload.rep5.vr2_1.max,
            p95: msg.payload.rep5.vr2_1.p95,
            p90: msg.payload.rep5.vr2_1.p90,
            p85: msg.payload.rep5.vr2_1.p85
        },
        tags: {
            plot: "rep5"
        },
        timestamp: new Date()
    },
    
    // Rep5_vr3_1
    {
        measurement: "vr3_1",
        fields: {
            timepi: msg.payload.rep5.vr3_1.timestamp,
            mean: msg.payload.rep5.vr3_1.mean,
            median: msg.payload.rep5.vr3_1.median,
            std: msg.payload.rep5.vr3_1.std,
            max: msg.payload.rep5.vr3_1.max,
            p95: msg.payload.rep5.vr3_1.p95,
            p90: msg.payload.rep5.vr3_1.p90,
            p85: msg.payload.rep5.vr3_1.p85
        },
        tags: {
            plot: "rep5"
        },
        timestamp: new Date()
    },
    
    // Rep5_vr4_1
    {
        measurement: "vr4_1",
        fields: {
            timepi: msg.payload.rep5.vr4_1.timestamp,
            mean: msg.payload.rep5.vr4_1.mean,
            median: msg.payload.rep5.vr4_1.median,
            std: msg.payload.rep5.vr4_1.std,
            max: msg.payload.rep5.vr4_1.max,
            p95: msg.payload.rep5.vr4_1.p95,
            p90: msg.payload.rep5.vr4_1.p90,
            p85: msg.payload.rep5.vr4_1.p85
        },
        tags: {
            plot: "rep5"
        },
        timestamp: new Date()
    }
];

return msg;